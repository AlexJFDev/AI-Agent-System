import socket

import sys

from io_streams import HOST, PORT

from games.oregon_trail import start_game

def run_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.bind((HOST, PORT))
        server_sock.listen(1)
        print(f"Server listening on {host}:{port}")

        client_sock, client_addr = server_sock.accept()
        print(f"Connection from {client_addr}")

        client_in = client_sock.makefile(mode="r")
        client_out = client_sock.makefile(mode="w")
        
        sys.stdin = client_in
        sys.stdout = client_out

        start_game()

if __name__ == "__main__":
    run_server(HOST, PORT)