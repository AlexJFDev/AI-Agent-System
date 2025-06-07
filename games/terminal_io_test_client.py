import socket
from io_streams import SocketIO, HOST, PORT

import threading

def run_client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock_io = SocketIO(sock)

        def receive_loop():
            while True:
                # line = sock_io.readline()
                # if not line:
                #     print("Connection closed")
                #     break
                ch = sock_io.read(1)
                if not ch:
                    print("connection closed")
                    break
                print(ch, end="", flush=True)

        threading.Thread(target=receive_loop, daemon=True).start()

        while(True):
            sock_io.write(f"{input()}\n")

if __name__ == "__main__":
    run_client(HOST, PORT)