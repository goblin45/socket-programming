import socket 

HOST = 'localhost'
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

data = client_socket.recv(1024).decode()
print("The date is:", data[:10])
print("The time is:", data[11:-7])

client_socket.close()