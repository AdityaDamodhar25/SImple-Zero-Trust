import socket

HOST = '35.78.69.205'
PORT = 54321

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

	s.connect((HOST, PORT))
	sending_data = b'Hello World'
	s.sendall(sending_data)
	data = s.recv(1024)
	print(f"Received {data!r}")



