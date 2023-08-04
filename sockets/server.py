import socket
import bcrypt

pw = "Password123"
hashed = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 9001

s.bind((host, port))
s.listen()

client, addr = s.accept()
print(f"Connection received from {addr}")
while True:
    data = "Welcome to the Server, what is the password?"
    client.sendall(str.encode(data))
    msg = client.recv(1024).decode()
    if bcrypt.checkpw(msg.encode(), hashed):
        data = ("Access Granted, Continue...")
        client.sendall(str.encode(data))
        while True:
            msg = client.recv(1024).decode()
            print(msg)
            data = input()
            client.sendall(str.encode(data))
            if msg == "":
                client.close()
                print(f"Connection with {addr} closed.")
    else:
        data = ("Access Denied, Goodbye.")
        client.sendall(str.encode(data))
        client.close()
    if not msg:
        break
client.close()
print(f"Connection with {addr} closed.")
