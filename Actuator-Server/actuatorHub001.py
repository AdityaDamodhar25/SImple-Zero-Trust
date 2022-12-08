import socket
import json
HOST = '18.183.218.145'
PORT = 54321


func_names = ['smoke','dis','dep','temp','hum','light']
i = 0
l = len(func_names)

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        text = func_names[i]
        i = (i+1)%l
        sending_data = text.encode('UTF-8')
        s.sendall(sending_data)
        while True:
            data = s.recv(1024)
            if not data:
                break
            print('Received Data')
            D = json.loads(data.decode('utf-8'))
            print(f"Received {D}")



