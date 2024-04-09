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

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = (HOST, PORT)
client.connect(server)

message = input("Enter message to be sent: ")
crc = calculate_crc(message.encode())

client.sendall(message.encode() + bytes([crc]))

client.close()