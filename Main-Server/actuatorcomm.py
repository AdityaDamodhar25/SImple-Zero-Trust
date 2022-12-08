from pandas import *
import socket
import json

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
i = 1


def smoke(i):
    i_ = i-1
    abs_val = smoke_data[i_]
    rel = smoke_data[0:i]
    avg_val = sum(rel)
    return (abs_val, avg_val)

def dis(i):
    i_ = i-1
    abs_val = dis_data[i_]
    rel = dis_data[0:i]
    avg_val = sum(rel)
    return (abs_val, avg_val)

def dep(i):
    i_ = i-1
    abs_val = dep_data[i_]
    rel = dep_data[0:i]
    avg_val = sum(rel)
    return (abs_val, avg_val)

def temp(i):
    i_ = i-1
    abs_val = temp_data[i_]
    rel = temp_data[0:i]
    avg_val = sum(rel)
    return (abs_val, avg_val)

def hum(i):
    i_ = i-1
    abs_val = hum_data[i_]
    rel = hum_data[0:i]
    avg_val = sum(rel)
    return (abs_val, avg_val)

def light(i):
    i_ = i-1
    abs_val = light_data[i_]
    rel = light_data[0:i]
    avg_val = sum(rel)
    return (abs_val, avg_val)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    while True:
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                param = data.decode('UTF-8')
                (abs_val, avg_val) = (0,0)
                if param == 'smoke':
                    (abs_val,avg_val) = smoke(i)
                    i+=1
                elif param == 'dis':
                    (abs_val,avg_val) = dis(i)
                    i+=1
                elif param == 'dep':
                    (abs_val,avg_val) = dep(i)
                    i+=1
                elif param == 'temp':
                    (abs_val,avg_val) = temp(i)
                    i+=1
                elif param == 'hum':
                    (abs_val,avg_val) = hum(i)
                    i+=1
                elif param == 'light':
                    (abs_val,avg_val) = light(i)
                    i+=1
                else:
                    continue
                sending_data = {'abs_val':abs_val, 'avg_val':avg_val}
                sending_data_encoded = json.dumps(sending_data).encode('UTF-8')
                conn.sendall(sending_data_encoded)
                print("Sent Data")

