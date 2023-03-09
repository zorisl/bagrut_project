import socket

HOST = 'localhost'
PORT = 5000

users = {'admin': 'password'}

def authenticate_user(username, password):
    if username in users and users[username] == password:
        return True
    else:
        return False

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f'Server listening on {HOST}:{PORT}...')

    while True:
        conn, addr = s.accept()
        print(f'Client connected from {addr}')

        with conn:
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break
                username, password = data.split(',')
                if authenticate_user(username, password):
                    conn.sendall(b'Welcome,' + username.encode())
                else:
                    conn.sendall(b'Invalid username or password')
