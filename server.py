import socket
import json
from icecream import ic
from time import sleep

HOST = "192.168.0.102"
PORT = 9090
SERVER_LOGIN = "admin1"
SERVER_PASSWORD = "32Ca9b"
resp1 = {"result": "Wrong password!"}
resp2 = {"result": "Wrong login!"}
resp3 = {"result": "Connection success!"}
resp4 = {"result": "Wrong"}
resp5 = {"result": "Exception happened during login"}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, adr = s.accept()

    with conn:
        print(f"Connected by: IP: {adr[0]}")
        while True:
            data = conn.recv(1024)
            data = data.decode()

            if not data:
                break
            else:
                # odczyt danych
                resp = json.loads(data)
                print("Data correct: ", resp)
                
                # if Login OK
                if resp['login'] == SERVER_LOGIN:
                    print("Login correct")
                    
                    if resp['password'] == SERVER_PASSWORD:
                        print("Login and password correct")
                        conn.sendall(json.dumps({"result": "Connection success!"}).encode())
                    elif resp['password'] == "":
                        conn.sendall(json.dumps({"result": "Wrong password!"}).encode())
                    elif SERVER_PASSWORD.startswith(resp['password']):
                        print("Login correct and check letter:")
                        ic(resp['password'])
                        sleep(0.1)
                        conn.sendall(json.dumps({"result": "Exception happened during login"}).encode())
                    else:
                        print("Wrong password!")
                        conn.sendall(json.dumps({"result": "Wrong password!"}).encode())

                # Wrong login!
                else:
                    print("Wrong, send feedback")
                    
                    conn.sendall(json.dumps({"result": "Wrong login!"}).encode())


# python server.py