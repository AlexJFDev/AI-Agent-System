import io
import socket
import codecs

from sys import __stdout__

def std_print(message):
    print(message, file=__stdout__)

class SocketIO(io.TextIOBase):
    def __init__(self, connection: socket.socket, encoding: str = "utf-8", newline: str = "\n", message_delimiter: bytes = b"\0"):
        """
        Wraps a connected socket.socket and presents a TextIOBase-compatible interface.
        - `connection` must already be a connected, blocking socket.
        - `encoding` is the character encoding used for .read/.write (default "utf-8").
        - `newline` controls how newline translation is (emulates TextIOBase's `newline`).
        """
        if not SocketIO._is_connected_socket(connection):
            raise ValueError("Socket must be a connected communication socket")
        self._sock = connection
        self._encoding = encoding
        self._newline = newline
        # Decoder to handle partial multibyte sequences:
        self._decoder = codecs.getincrementaldecoder(self._encoding)()
        # Internal text buffer (decoded) for reads:
        self._text_buffer = ""
        # Internal byte buffer for writes:
        self._write_buffer = b""
        self._closed = False

    @staticmethod
    def _is_connected_socket(sock: socket.socket) -> bool:
        try:
            sock.getpeername()
            return True
        except OSError:
            return False

    #
    # ===== Reading methods =====
    #

    def readable(self) -> bool:
        return True

    def _fill_text_buffer(self, min_chars: int = 1) -> None:
        """
        Read raw bytes from the socket and decode into the internal text buffer
        until we have at least `min_chars` characters in _text_buffer or the
        socket is closed on the other end.
        """
        # Keep looping until we have enough decoded chars or the socket is closed.
        while len(self._text_buffer) < min_chars:
            try:
                chunk = self._sock.recv(4096)
            except (BlockingIOError, InterruptedError):
                # No data available right now; break out so we don't spin
                break
            if not chunk:
                # Peer has closed the connection
                # Decode any final bytes
                tail = self._decoder.decode(b"", final=True)
                if tail:
                    self._text_buffer += tail
                break
            # Decode what we got (may be a partial multibyte sequence)
            decoded = self._decoder.decode(chunk)
            if decoded:
                self._text_buffer += decoded

    def read(self, size: int = -1) -> str:
        """
        Read up to `size` characters (decoded). If size < 0, read until EOF (socket close).
        """
        if self._closed:
            raise ValueError("I/O operation on closed file.")
        
        if size is None:
            size = -1

        if size > 0:
            # Fill `self._text_buffer` up to `size`
            self._fill_text_buffer(size)
            result = self._text_buffer[:size]
            self._text_buffer = self._text_buffer[size:]
            return result
        else:
            # If user wants all data until EOF:
            # Keep reading until the socket is fully closed by the peer
            while True:
                try:
                    chunk = self._sock.recv(4096)
                except (BlockingIOError, InterruptedError):
                    break
                if not chunk:
                    break
                self._text_buffer += self._decoder.decode(chunk)
            
            # Decode any final buffered bytes
            self._text_buffer += self._decoder.decode(b"", final=True)
            result = self._text_buffer
            self._text_buffer = ""
            return result

    def readline(self, limit: int = -1) -> str:
        """
        Read until newline (self._newline) or up to `limit` characters.
        """
        if self._closed:
            raise ValueError("I/O operation on closed file.")

        newline_char = self._newline
        # First, see if newline is already in the buffer:
        idx = self._text_buffer.find(newline_char)
        # Keep filling until we see newline or reach EOF / limit
        while idx < 0:
            # Attempt to read more bytes and decode
            self._fill_text_buffer(min_chars=1)
            idx = self._text_buffer.find(newline_char)
            # If still not found, but no more data is forthcoming, break
            if not self._text_buffer:
                break

        if idx >= 0:
            # We found a newline at position idx
            end = idx + len(newline_char)
            line = self._text_buffer[:end]
            if 0 <= limit < len(line):
                # If limit is smaller than the full line, truncate
                line = line[:limit]
                self._text_buffer = self._text_buffer[len(line):]
                return line
            # Otherwise consume up to newline
            self._text_buffer = self._text_buffer[end:]
            return line if limit < 0 else line[:limit]
        else:
            # No newline was found, so return whatever is in buffer (possibly empty)
            if limit >= 0:
                result = self._text_buffer[:limit]
                self._text_buffer = self._text_buffer[len(result):]
                return result
            else:
                result = self._text_buffer
                self._text_buffer = ""
                return result

    def readlines(self, hint: int = -1):
        """
        Collect all lines (as in TextIOBase) until EOF or until total size >= hint.
        """
        if self._closed:
            raise ValueError("I/O operation on closed file.")

        lines = []
        total = 0
        while True:
            line = self.readline()
            if not line:
                break
            lines.append(line)
            total += len(line)
            if 0 <= hint <= total:
                break
        return lines

    #
    # ===== Writing methods =====
    #

    def writable(self) -> bool:
        return True

    def write(self, s: str) -> int:
        """
        Buffer the given string. Return the number of characters “accepted”.
        Actual sending happens on .flush().
        """
        if self._closed:
            raise ValueError("I/O operation on closed file.")
        if not isinstance(s, str):
            raise TypeError("write() argument must be str, not {}".format(type(s).__name__))

        data_bytes = s.encode(self._encoding)
        self._write_buffer += data_bytes
        if b"\n" in data_bytes:
            self.flush()

        # Return number of characters written (not bytes)
        return len(s)

    def flush(self) -> None:
        """
        Send out any buffered data. Blocks until all bytes are sent.
        """
        if self._closed:
            raise ValueError("I/O operation on closed file.")
        if not self._write_buffer:
            return
        
        total_sent = 0
        buf = self._write_buffer
        # We use sendall, but wrap it to catch errors
        try:
            self._sock.sendall(buf)
            total_sent = len(buf)
        except OSError as e:
            raise io.BlockingIOError(f"Error while sending data: {e}") from e
        finally:
            # Clear buffer whether it succeeded or not (TextIOBase expects that behavior)
            self._write_buffer = b""

    #
    # ===== Other properties / methods =====
    #

    @property
    def encoding(self) -> str:
        return self._encoding

    @property
    def newline(self) -> str:
        return self._newline

    def isatty(self) -> bool:
        # A socket is not a TTY
        return False

    def seekable(self) -> bool:
        return False

    def tell(self) -> int:
        raise OSError("tell() not supported on a socket-based stream")

    def seek(self, offset, whence=io.SEEK_SET):
        raise OSError("seek() not supported on a socket-based stream")

    def close(self) -> None:
        """
        Flush any pending writes, then close the socket and mark this TextIO as closed.
        """
        if not self._closed:
            try:
                # Attempt to flush any pending writes
                try:
                    self.flush()
                except Exception:
                    pass
                self._sock.shutdown(socket.SHUT_RDWR)
            except Exception:
                pass
            finally:
                self._sock.close()
                self._closed = True

    @property
    def closed(self) -> bool:
        return self._closed

    def __enter__(self):
        if self._closed:
            raise ValueError("I/O operation on closed file.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

class TextBuffer:
    def __init__(self, buffer:str="", delimiter:str="\n"):
        self._buffer = buffer
        self._delimiter = delimiter

    def push(self, text: str) -> None:
        self._buffer += text

    def peek(self, n: int = None) -> str:
        if n is None: return self._buffer
        return self._buffer[:n]

    def pop(self, n: int = None) -> str:
        """
        Removes and returns a portion of the buffer up to and including the delimiter, or up to `n` characters.

        Args:
            n (int, optional): The maximum number of characters to remove from the buffer. If not specified, removes up to and including the delimiter.

        Returns:
            str: The removed portion of the buffer.

        Notes:
            - If the delimiter is not found, removes up to `n` characters if specified, otherwise removes the entire buffer.
            - If `n` is specified and less than the position of the delimiter, removes only `n` characters.
        """
        index = self._buffer.find(self._delimiter)
        if index >= 0:
            index += len(self._delimiter)
        if n is not None and n < index:
            index = n
        if index < 0:
            index = len(self)
        part = self._buffer[:index]
        self._buffer = self._buffer[index:]
        return part
    
    def __len__(self) -> int:
        return len(self._buffer)
    
    def is_empty(self) -> bool:
        return len(self) == 0
    
    def clear(self) -> None:
        self._buffer = ""

    def __repr__(self):
        return f"TextBuffer delimiter={repr(self._delimiter)} buffer={repr(self._buffer)}"