import socket

HOST = 'localhost'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))
print("Server is listening...")

data, addr = server.recvfrom(1024)
filename = 'rec-' + data.decode()

file = open(filename, 'wb')
while True:
    data, addr = server.recvfrom(1024)
    if not data:
        break
    file.write(data)
    file.flush()

server.close()
print(f'File received: {filename}')

file = open(filename, 'r', encoding='UTF-8')
print(file.read())