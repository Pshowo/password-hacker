import socket

HOST = "192.168.0.102"
PORT = 9090

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
                data = data.decode()
                print("Data:", data)

# python server.py