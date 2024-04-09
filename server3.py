import socket 

HOST = 'localhost'
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen()
print("Server listenting...")
conn, addr = server_socket.accept()
print('Connected by', addr)

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print('Client message:', data)
    reverse = ""
    for i in range(len(data) - 1, -1, -1):
        reverse += data[i]
    conn.sendall(reverse.encode())