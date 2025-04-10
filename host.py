import socket
import time
import json

BROADCAST_IP = '255.255.255.255'
PORT = 50000

while True:
    print("s")
    message = json.load(open('message.json', 'r'))
    if message.get('message') == None:

        print("Please initialize the LocalDrop Using 'localdrop init' first.")
    else:
        if time.time() > message.get('expireTime'):
            with open('message.json', 'w') as file:
                file.write("{}")

        else:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            data = json.dumps(message).encode('utf-8')
            sock.sendto(data, (BROADCAST_IP, PORT))
