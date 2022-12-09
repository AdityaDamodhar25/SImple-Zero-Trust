from csv import writer
from csv import DictWriter
from pandas import *
import socket
import hashlib
import rsa
import pickle
import time

HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
PORT_S = 65432  # Port to listen on (non-privileged ports are > 1023)
PORT_A = 54321


Logs_Data = read_csv("/home/ubuntu/Logs/logs.csv")
field_names = ['smoke_i', 'dis_i', 'dep_i', 'temp_i', 'hum_i', 'light_i']

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
    avg_val = sum(rel)/i
    return (abs_val, avg_val)

def dis(i):
    i_ = i-1
    abs_val = dis_data[i_]
    rel = dis_data[0:i]
    avg_val = sum(rel)/i
    return (abs_val, avg_val)

def dep(i):
    i_ = i-1
    abs_val = dep_data[i_]
    rel = dep_data[0:i]
    avg_val = sum(rel)/i
    return (abs_val, avg_val)

def temp(i):
    i_ = i-1
    abs_val = temp_data[i_]
    rel = temp_data[0:i]
    avg_val = sum(rel)/i
    return (abs_val, avg_val)

def hum(i):
    i_ = i-1
    abs_val = hum_data[i_]
    rel = hum_data[0:i]
    avg_val = sum(rel)/i
    return (abs_val, avg_val)

def light(i):
    i_ = i-1
    abs_val = light_data[i_]
    rel = light_data[0:i]
    avg_val = sum(rel)/i
    return (abs_val, avg_val)



s_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_s.bind((HOST, PORT_S))
s_a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_a.bind((HOST, PORT_A))


while(True):
    s_s.listen()
    conn, addr = s_s.accept()
    with conn:
        conn.sendall(b'go')
        print(f"Connected by {addr}")
        data = conn.recv(1024)
        Pass = data.decode('utf-8')
        sensorHub_pass = hashlib.sha256(b'12345').hexdigest()
        if (Pass == sensorHub_pass):
            conn.sendall(b'go')
            print('Authenticated')
        else:
            conn.sendall(b'no go')
            conn.close()
            try:
                conn.sendall(b'ping')
                print('Still connected')
            except:
                print('Disconnected')
            print('Not Authenticated')
            continue
        pub_ser_1,priv_ser_1 = rsa.newkeys(1024)
        conn.sendall(pickle.dumps(pub_ser_1))
        data_enc = conn.recv(2048)
        data = rsa.decrypt(data_enc,priv_ser_1)
        D1 = pickle.loads(data)
        data_enc = conn.recv(2048)
        data = rsa.decrypt(data_enc,priv_ser_1)
        D2 = pickle.loads(data)

        D = {**D1, **D2}

        with open('/home/ubuntu/Logs/logs.csv','a') as f_object:
            dictw_obj = DictWriter(f_object, fieldnames = field_names)
            dictw_obj.writerow(D)
            f_object.close()
        conn.close()
        try:
            conn.sendall(b'ping')
            print('Still open')
        except:
            print('Closed')

    s_a.listen()
    conn, addr = s_a.accept()
    with conn:
        conn.sendall(b'go')
        print(f"Connected by {addr}")
        data = conn.recv(1024)
        Pass = data.decode('utf-8')
        sensorHub_pass = hashlib.sha256(b'12345').hexdigest()
        if (Pass == sensorHub_pass):
            conn.sendall(b'go')
            print('Authenticated')
        else:
            conn.sendall(b'no go')
            conn.close()
            try:
                conn.sendall(b'ping')
                print('Still connected')
            except:
                print('Disconnected')
            print('Not Authenticated')
            continue
        print(f"Connected by {addr}")
        pub_ser_2,priv_ser_2 = rsa.newkeys(1024)
        conn.sendall(pickle.dumps(pub_ser_2))
        pub_act_b = conn.recv(1024)
        pub_act = pickle.loads(pub_act_b)
        data_b = conn.recv(1024)
        data = rsa.decrypt(data_b,priv_ser_2)
        [param,i] = data.decode('UTF-8').split(',')
        i = int(i)
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

        sending_data = {'Parameter':param, 'abs_val':abs_val, 'avg_val':avg_val}
        sending_data_encoded = pickle.dumps(sending_data)
        sending_data_enc = rsa.encrypt(sending_data_encoded, pub_act)
        conn.sendall(sending_data_enc)
        print("Sent Data")
        conn.close()
        try:
            conn.sendall(b'ping')
            print('Still open')
        except:
            print('Closed')
        
        time.sleep(20)
