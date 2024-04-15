import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define server address and port
server_address = ('localhost', 8080)

# Bind the socket to the server address
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print("Server is listening for connections...")

# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Receive data from the client
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print(f"Received: {data.decode()}")

# Close the connection
client_socket.close()
server_socket.close()
