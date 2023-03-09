# echo-client.py

import socket

HOST = "192.168.7.90"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
DISCONNECT_MESSAGE = "!DISCONECT"
FILE_SHARE_MESSAGE = '!FILE'
FORMAT = 'UTF-8'
SIZE = 1024


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    connected = True
    while connected:
        tekst = input('geef input: ').encode('FORMAT')   #encode en decode voor binair formaat
        s.sendall(tekst)
        data = s.recv(1024)
        print(data.decode('FORMAT'))
        if tekst.decode('FORMAT') == DISCONNECT_MESSAGE:
            # opening and reading file
            file = open('data/test_data.txt', 'r')
            data = file.read()

            # Sending the filename to the server.
            s.send("test_data.txt".encode(FORMAT))
            msg = s.recv(SIZE).decode(FORMAT)
            print(f"[SERVER]: {msg}")

            # Sending the file data to the server.
            s.send(data.encode(FORMAT))
            msg = s.recv(SIZE).decode(FORMAT)
            print(f"[SERVER]: {msg}")

            # Closing the file..
            file.close()

            # Closing the connection from the server.
            connected = False

        elif tekst.decode('FORMAT') == DISCONNECT_MESSAGE:
            connected = False