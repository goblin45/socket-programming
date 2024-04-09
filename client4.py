import socket 

HOST = 'localhost'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

filename = input("Enter filename to send: ")

file = open(filename, 'rb')
client.sendto(filename.encode(), (HOST, PORT))

while True: 
    data = file.read(1024)
    print(data)
    if not data:
        break
    client.sendto(data, (HOST, PORT))

print(f'File {filename} sent to server successfully.')
client.close()
