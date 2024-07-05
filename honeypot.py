import socket
import threading

def handle_client(client_socket):
    with client_socket:
        print(f"Connection from {client_socket.getpeername()}")
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode('utf-8')})
            client_socket.sendall(b"ACK\n)

def start_honeypot(host='0.0.0.0', port-9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Listening on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Threat(target=handle_client, args=(client_socket,))
        client_handler.start()


if __name__ == "__main__":
    start_honeypot()
