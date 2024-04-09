import socket 

HOST = 'localhost'
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen()
print("Server listening...")

conn, addr = server_socket.accept()

expected_seq = 0

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    seq_num, message = data.split(':', 1)
    if int(seq_num) == expected_seq:
        print("Received message:", message)
        expected_seq = (expected_seq + 1) % 2
        conn.sendall(str(expected_seq).encode())
    else:
        print('Packet with unexpected sequence number:', seq_num)
        conn.sendall(str(expected_seq).encode())