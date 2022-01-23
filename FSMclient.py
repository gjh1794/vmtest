# client
import socket
import subprocess

#note: set host to 127.0.0.1 if testing on local machine. Otherwise, use ifconfig/ipconfig
#to find server machine and set accordingly.
host = '127.0.0.1'
port = 99

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect((host, port))

while True:
    user_command = input("Enter command: ")
    lst = user_command.split()
    if lst[0] == 'quit':
        client_sock.send(user_command.encode())
        break
    elif lst[0] == 'write':
        client_sock.send(user_command.encode())
        ok = client_sock.recv(32).decode()
        if ok == 'OK':
            content = ""
            while True:
                line = input("> ")
                content += line+"\n"
                if line == "":
                    break            
            print("dbg:", content)
                   
            client_sock.send(content.encode())
        else: #ERR
            print(f"{lst[1]}: directory does not exist")
    elif lst[0] == 'cat':
        client_sock.send(user_command.encode())
        msg_from_server = client_sock.recv(1024)
        print(msg_from_server[:-2].decode())
    elif lst[0] == 'pwd':
        client_sock.send(user_command.encode())
        msg_from_server = client_sock.recv(1024)
        print(msg_from_server.decode())
    elif lst[0] == 'ls':
        client_sock.send(user_command.encode())
        msg_from_server = client_sock.recv(1024)
        print(msg_from_server.decode())
    elif lst[0] == 'mkdir':
        client_sock.send(user_command.encode())
        print(client_sock.recv(1024).decode())
    elif lst[0] == 'cd':
        client_sock.send(user_command.encode())
        print(client_sock.recv(1024).decode())
    else:
        print(lst[0]+": invalid command")
client_sock.close()


