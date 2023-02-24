# echo-server.py

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
DISCONNECT_MESSAGE = "!DISCONECT"
ADDR = (HOST, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)


def handle_client(conn, addr):
    print(f"[Connected] by {addr}")

    connected = True
    while connected:
        data = conn.recv(1024)
        if data.decode('UTF-8') == DISCONNECT_MESSAGE:
            connected = False
            response = "[Disconected]".encode('UTF-8')
        else:
            print(f"[{addr}]", data.decode('UTF-8'))
            response = "[MessageReceived]".encode('UTF-8')

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