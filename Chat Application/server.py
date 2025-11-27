import socket

def server_program():
    host = "127.0.0.1"  
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    print("Server listening on", host, ":", port)

    conn, address = server_socket.accept()
    print("Connection from:", address)

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("From connected user:", data)
        data = input(" -> ")
        conn.send(data.encode())

    conn.close()

if __name__ == "__main__":
    server_program()

