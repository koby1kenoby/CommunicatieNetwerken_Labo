import threading
import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDR = (HOST, PORT)
connected = False

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)

def recv_msg(conn, addr):
    global connected
    while connected:
        recv_msg = conn.recv(1024)
        print(f"[{addr}] ->", recv_msg.decode('UTF-8'))
        if recv_msg.decode('UTF-8') == DISCONNECT_MESSAGE:
            conn.sendall("[Disconnected]".encode('UTF-8'))
            conn.close()
            connected = False
            print(f"[{addr}] ->", "CLOSED THE CONNECTION!")

def send_msg(conn, addr):
    global connected
    while connected:
        try:
            send_msg = input(str())
            conn.sendall(send_msg.encode('UTF-8'))
        except:
            print("[No Client] can't send message when no client is connected")

def start():
    global connected
    while not connected:
        conn, addr = s.accept()
        print(f"[Connected] client {addr} connected")
        connected = True
        t_recv = threading.Thread(target=recv_msg, args=(conn, addr))
        t_recv.start()
        t_send = threading.Thread(target=send_msg, args=(conn, addr))
        t_send.start()

print("[STARTING] server is starting...")
s.listen()
print(f"[LISTENING] Server is listening on {HOST}")

while True:
    start()
