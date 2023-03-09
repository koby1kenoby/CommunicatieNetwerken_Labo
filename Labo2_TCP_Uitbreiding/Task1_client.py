# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
DISCONNECT_MESSAGE = "!DISCONECT"


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    connected = True
    while connected:
        tekst = input('geef input: ').encode('UTF-8')   #encode en decode voor binair formaat 
        s.sendall(tekst)
        data = s.recv(1024)
        print(data.decode('UTF-8'))
        if tekst.decode('UTF-8') == DISCONNECT_MESSAGE:
            connected = False