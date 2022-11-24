from numpy import *
import socket

HOST = '0.0.0.0'
PORT = 54321

Logs_Data = read_csv("/home/ubuntu/Logs/logs.csv")
field_names = ['smoke_i', 'dis_i', 'dep_i', 'temp_i', 'hum_i', 'light']

smoke_data = Logs_Data['smoke_i'].tolist()
dis_data = Logs_Data['dis_i'].tolist()
dep_data = Logs_Data['dep_i'].tolist()
temp_data = Logs_Data['temp_i'].tolist()
hum_data = Logs_Data['hum_i'].tolist()
light_data = Logs_Data['light_i'].tolist()

l = len(smoke_data)

def smoke(i):
    i_ = i-1
    abs_val = smoke_data[i_]
    rel = smoke_data[0:i]
    avg_val = sum(rel)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	conn, addr = s.accept()
	with conn:
		print(f"Connected by {addr}")
		while True:
			data = conn.recv(1024)
			if not data:
				break
			print(data)
		conn.sendall(data)
