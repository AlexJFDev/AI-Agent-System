import socket
from __init__ import SocketIO, GAME_HOST, GAME_PORT

import threading

def run_client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock_io = SocketIO(sock)

        def receive_loop():
            while True:
                ch = sock_io.read(1)
                if not ch:
                    # EOF (socket closed)
                    print("Connection closed")
                    break
                # Print it immediately, without waiting for a newline
                print(ch, end='', flush=True)

        threading.Thread(target=receive_loop, daemon=True).start()

        while(True):
            sock_io.write(f"{input()}\n")

if __name__ == "__main__":
    run_client(GAME_HOST, GAME_PORT)