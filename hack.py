import sys
import socket
"""Args: Host, port, message"""

socket_1 = socket.socket()
address = (sys.argv[1], int(sys.argv[2]))

socket_1.connect(address)
data = sys.argv[3].encode()
socket_1.send(data)
print("Send:", data)

response = socket_1.recv(1024)
print("Response: ", response.decode())

socket_1.close()

# python hack.py 192.168.0.102 9090 qwerty