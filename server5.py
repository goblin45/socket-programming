import socket 

HOST = 'localhost'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()
print("Server is listening...")

conn, addr = server.accept()
print("Connected to client at", addr[0] + ":" + addr[1])

filename = 'rec-' + conn.recv(1024).decode()

with open(filename, 'wb') as f:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)
        f.flush()

print("File received successfully!")

conn.close()