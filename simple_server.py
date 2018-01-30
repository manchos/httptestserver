import socket

def server_forever():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('185.87.194.206', 9004))
    server_socket.listen()

    while True:
        client_connection, client_address = server_socket.accept()
        request = client_connection.recv(1024)
        print(client_address)
        print(request)


        client_connection.sendall(b"HTTP/1.1 200 OK\n\nHello!")
        client_connection.close()

server_forever()