from csv import writer
from csv import DictWriter
from pandas import *
import socket
import hashlib
import rsa
import pickle
import time


field_names = ['dis_i']

with open('/home/ubuntu/Logs/logs.csv','w') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(field_names)
    f_object.close

HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
PORT_S = 65432  # Port to listen on (non-privileged ports are > 1023)
PORT_A = 54321


def reading(i,log_data):
    i_ = i-1
    abs_val = log_data[i_]
    rel = log_data[0:i]
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
        D = pickle.loads(data)
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

    Logs_Data = read_csv("/home/ubuntu/Logs/logs.csv")
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
        log_data = Logs_Data['dis_i'].tolist()
        (abs_val,avg_val) = reading(i,log_data)
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
        
        time.sleep(5)
