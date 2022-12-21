import socket

HOST = '43.207.32.202'
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((HOST, PORT))
d = s.recv(1024)
s.sendall(b'Logs,Data')
print('Sending request for Logs Data')
data = s.recv(2048)
print('Received Data:', data)
