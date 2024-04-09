import socket 
import datetime

HOST = 'localhost'
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen()
print("Server is listening...")

conn, addr = server_socket.accept()

conn.sendall(str(datetime.datetime.now()).encode())
print("Date and time sent.")

conn.close()