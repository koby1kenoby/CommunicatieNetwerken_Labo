import threading
import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
DISCONNECT_MESSAGE = "!DISCONNECT"
connected = True


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("[Connected to server]")

def recv_msg():
    global connected
    while connected:
        recv_msg = s.recv(1024)
        print("[Server] ->",recv_msg.decode('UTF-8'))

def send_msg():
    global connected
    while connected:
        send_msg = input(str())
        s.send(send_msg.encode('UTF-8'))
        if send_msg == DISCONNECT_MESSAGE:
            connected = False

t = threading.Thread(target=recv_msg)
t.start()

send_msg()
