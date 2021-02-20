import socket

HOST = "192.168.0.102"
PORT = 9090
SERVER_PASSWORD = "adm"

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
                if data.decode() == SERVER_PASSWORD:
                    conn.sendall("Connection success!".encode())
                else:
                    conn.sendall(data)

# python server.py