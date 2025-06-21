import socket
from io_streams import HOST, PORT

import threading

def run_client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        server_in = sock.makefile(mode="r")
        server_out = sock.makefile(mode="w")

        def receive_loop():
            while True:
                ch = server_in.read(1)
                if not ch:
                    print("connection closed")
                    break
                print(ch, end="", flush=True)

        threading.Thread(target=receive_loop, daemon=True).start()

        while(True):
            server_out.write(f"{input()}\n")
            server_out.flush()

if __name__ == "__main__":
    run_client(HOST, PORT)