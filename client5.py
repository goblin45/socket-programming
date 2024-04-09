import socket 

HOST = 'localhost'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = (HOST, PORT)

client.connect(server)

filename = input("Enter the name of the file to be sent: ")
file = open(filename, 'rb')

client.sendall(filename.encode())
while True:
    data = file.read(1024)
    if not data:
        break
    client.sendall(data)

print("File sent successfully!")

client.close()