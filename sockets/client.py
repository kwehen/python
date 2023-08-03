import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 9001

s.connect((host, port))

while True:
    msg = s.recv(1024).decode()
    if not msg:
        break
    print(msg)
    data = input('Enter a message:')
    s.sendall(str.encode(data))

s.close()
print('Connection with server has been closed.')

# data = s.recv(1024).decode()
# print(data)
# s.close()
# print('Connection Closed')
