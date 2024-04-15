import socket 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)
print(f"Listening on {SERVER_HOST}:{SERVER_PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    request = client_socket.recv(1500).decode()
    print(f"{client_address[0]}:{client_address[1]} Connected")
    print(request)
    headers = request.split("\n")
    first_header_components = headers[0].split()  # Corrected this line
    http_method = first_header_components[0]
    path = first_header_components[1]
    if http_method=='GET':
        if path == "/":
            path = "/index.html"
            fin = open("index.html")
            content = fin.read()
            fin.close()
            # STATUS LINE
            # HEADERS
            # MESSAGE BODY
            response = f"HTTP/1.1 200 OK\n\n\n\n"+content
            client_socket.sendall(response.encode())
            client_socket.close()
        else:
            response = "HTTP/1.1 404 NOT FOUND\n\n\n\n"
        client_socket.sendall(response.encode())
        client_socket.close()
