import socket

import sys

from io_streams import SocketIO, HOST, PORT

from games.oregon_trail import start_game

def true_print(message):
    print(message, file=sys.__stdout__)

def run_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.bind((HOST, PORT))
        server_sock.listen(1)
        print(f"Server listening on {host}:{port}")

        client_sock, client_addr = server_sock.accept()
        print(f"Connection from {client_addr}")

        with SocketIO(client_sock) as client_sock:
            sys.stdin = client_sock
            sys.stdout = client_sock

            start_game()

if __name__ == "__main__":
    run_server(HOST, PORT)