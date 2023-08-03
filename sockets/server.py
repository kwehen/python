import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 9001

s.bind((host, port))

s.listen()

client, addr = s.accept()
print(f"Connection received from {addr}")
while True:
    data = input('Enter a message:')
    client.sendall(str.encode(data))
    msg = client.recv(1024).decode()
    if not msg:
        break
    print(msg)

client.close()
print(f'Connection with {addr} has been closed.')

# data = "This is a test, thank you for your connection"
# client.sendall(str.encode(data))
# client.close
# print(f'Connection with {addr} has been closed')
