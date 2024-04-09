import socket 

HOST = 'localhost'
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

seq_num = 0
while True:
    message = input("Enter message to send (or 'quit' to exit): ")
    if message == 'quit':
        break
    data = f"{seq_num}:{message}"
    client_socket.sendall(data.encode())
    seq_num = (seq_num + 1) % 2

    ack = client_socket.recv(1024).decode()
    while int(ack) != seq_num:
        print(f"Timeout, re-sending message: {data}")
        client_socket.sendall(data.encode())
        ack = client_socket.recv(1024).decode()

client_socket.close()
    