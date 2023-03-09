# echo-server.py

import socket

HOST = "192.168.7.90"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
DISCONNECT_MESSAGE = "!DISCONECT"
FILESHARE_MESSAGE = "!FILE"
ADDR = (HOST, PORT)
SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)


def handle_client(conn, addr):
    print(f"[Connected] client {addr} connected")

    connected = True
    while connected:
        data = conn.recv(1024)
        if data.decode('UTF-8') == DISCONNECT_MESSAGE:
            connected = False
            response = "[Disconected]".encode('UTF-8')
        elif data.decode('UTF-8') == FILESHARE_MESSAGE:
            """ Receiving the filename from the client. """
            filename = conn.recv(SIZE).decode('UTF-8')
            print(f"[RECV] Receiving the filename.")
            file = open(filename, "w")
            conn.send("Filename received.".encode('UTF-8'))
            """ Receiving the file data from the client. """
            data = conn.recv(SIZE).decode('UTF-8')
            print(f"[RECV] Receiving the file data.")
            file.write(data)
            conn.send("File data received".encode('UTF-8'))
        else:
            print(f"[{addr}] ->", data.decode('UTF-8'))
            response = "[MessageReceived]".encode('UTF-8')

            connected = False
            response = "[Disconected]".encode('UTF-8')

        conn.sendall(response)
    
    print(f"[Disconected] client {addr} disconected")
    conn.close()


def start():
    s.listen()
    print(f"[LISTENING] Server is listening on {HOST}")
    while True:
        conn, addr = s.accept()
        handle_client(conn, addr)
        
print("[STARTING] server is starting...")
start()