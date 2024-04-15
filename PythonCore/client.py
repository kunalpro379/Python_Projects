import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 8080)

client_socket.connect(server_address)

message = "Hello, server!"
client_socket.sendall(message.encode())

client_socket.close()