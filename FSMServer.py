# Server
# Gregory Henigman
import socket
import subprocess
import os

#note: set HOST to 127.0.0.1 if testing on local machine. Otherwise, use ifconfig/ipconfig
#to find server machine and set accordingly.
HOST = '127.0.0.1'
PORT = 99

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            command = data.decode()
            #run the command through subprocess, then send back the output
            print(data)
            a = subprocess.run(command, capture_output=True)
            conn.sendall(a)
