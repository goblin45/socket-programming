import socket

HOST = 'localhost'
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
while True:
    message = input("Enter message to send (or 'quit' to exit): ")
    if message == 'quit':
        break
    client_socket.sendall(message.encode())
    data = client_socket.recv(1024).decode()
    print("Server response:", data)