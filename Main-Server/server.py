from csv import writer
from csv import DictWriter
import socket
import json

HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

field_names = ['smoke_i', 'dis_i', 'dep_i', 'temp_i', 'hum_i', 'light_i']



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))

	while(True):
		s.listen()
		conn, addr = s.accept()
		with conn:
			print(f"Connected by {addr}")
			while True:
				data = conn.recv(1024)
				if not data:
					break
				D = json.loads(data.decode('utf-8'))
				print(D)
				conn.sendall(data)
		print(D)
		with open('/home/ubuntu/Logs/logs.csv','a') as f_object:
			dictw_obj = DictWriter(f_object, fieldnames = field_names)
			dictw_obj.writerow(D)
			f_object.close()
