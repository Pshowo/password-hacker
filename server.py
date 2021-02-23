import socket
import json

HOST = "192.168.0.102"
PORT = 9090
SERVER_LOGIN = "username1"
SERVER_PASSWORD = "1234"
resp1 = {"result": "Wrong password!"}
resp2 = {"result": "Wrong login!"}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, adr = s.accept()

    with conn:
        print(f"Connected by: IP: {adr[0]}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            else:
                resp = json.loads(data.decode())
                print("Data:", resp)
                if resp['login'] == SERVER_LOGIN:
                    print("Login OK.")
                    conn.sendall(json.dumps(resp1).encode())
                else:
                    print("Wrong login")
                    conn.sendall(json.dumps(resp2).encode())

# python server.py