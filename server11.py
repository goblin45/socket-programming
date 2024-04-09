import socket 

def calculate_crc(message):
    crc = 0
    for byte in message:
        crc ^= byte
        for _ in range(8):
            if crc & 0x80:
                crc = (crc << 1) ^ 0x1D
            else:
                crc <<= 1
    return crc & 0xFF

HOST = 'localhost'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()
print("Server is listening...")

conn, addr = server.accept()
print("Connected by: ", addr)

data = conn.recv(1024)
message, received_crc = data[:-1], data[-1]

calculated_crc = calculate_crc(message)

if received_crc == calculated_crc:
    print("CRC check passed. Data integrity verified.")
    print(message.decode())
else:
    print("CRC check failed. Data has been corrupted.")

conn.close()
server.close()