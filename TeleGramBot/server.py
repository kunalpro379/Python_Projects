import socket
import threading
import random

clients = {}
waiting_clients = []

def handle_clients(client_socket):
    try:
        # Receive chat ID, name, and gender from the client
        chat_id = client_socket.recv(1024).decode()
        name = client_socket.recv(1024).decode()
        gender = client_socket.recv(1024).decode()

        # Print received data for debugging
        print("Received chat ID:", chat_id)
        print("Received name:", name)
        print("Received gender:", gender)

        # Store client information
        clients[chat_id] = (name, gender)

        # Add client to waiting list
        waiting_clients.append(client_socket)
        print("Waiting clients:", waiting_clients)

        # If there are at least two clients waiting, try to match them
        if len(waiting_clients) >= 2:
            male_clients = [client for client in waiting_clients if clients[client][1] == 'male']
            female_clients = [client for client in waiting_clients if clients[client][1] == 'female']
            print("Male clients:", male_clients)
            print("Female clients:", female_clients)
            
            if male_clients and female_clients:
                male_client = random.choice(male_clients)
                female_client = random.choice(female_clients)

                waiting_clients.remove(male_client)
                waiting_clients.remove(female_client)

                male_client.sendall("You are connected with a female user".encode())
                female_client.sendall("You are connected with a male user".encode())

                threading.Thread(args=(male_client, female_client)).start()

    except ConnectionResetError:
        print("Client disconnected unexpectedly.")
        if client_socket in waiting_clients:
            waiting_clients.remove(client_socket)
        client_socket.close()

    except Exception as e:
        print(f"Error: {e}")
        if client_socket in waiting_clients:
            waiting_clients.remove(client_socket)
        client_socket.close()


# def handle_conv(client1, client2):
#     try:
#         print(f"New conversation started between {clients[client1]} and {clients[client2]}")
#         while True:
#             msg = client1.recv(1024).decode()
#             if not msg:
#                 break
#             client2.sendall(msg.encode())

#             msg = client2.recv(1024).decode()
#             if not msg:
#                 break
#             client1.sendall(msg.encode())
#     except Exception as e:
#         print(f"Error: {e}")
#     finally:
#         if client1 in clients:
#             del clients[client1]
#         if client2 in clients:
#             del clients[client2]
#         client1.close()
#         client2.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        server_socket.bind(('0.0.0.0', 5050))
        server_socket.listen(5)
        print("Server listening on 0.0.0.0:5050")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"New connection from {client_address}")
            threading.Thread(target=handle_clients, args=(client_socket,)).start()
    except Exception as e:
        print(f"Error starting server: {e}")
    finally:
        server_socket.close()

# Start the server
start_server()
