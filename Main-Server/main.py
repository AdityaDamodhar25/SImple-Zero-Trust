from csv import writer
from csv import DictWriter
from pandas import *
import socket
import hashlib
import rsa
import pickle
import time


(priv_master, pub_master) = rsa.newkeys(512)


field_names = ['smoke_i', 'dis_i', 'dep_i', 'temp_i', 'hum_i', 'light_i']

with open('/home/ubuntu/Logs/logs.csv','w') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(field_names)
    f_object.close

HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
PORT_S = 65432  # Port to listen on (non-privileged ports are > 1023)
PORT_A = 54321


def reading(i,log_data):
    i_ = i-1
    abs_val_enc = bytes.fromhex(log_data[i_])
    abs_val = pickle.loads(rsa.decrypt(abs_val_enc, pub_master))
    return (abs_val )



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
        print('Shared Main Server Public Key to Sensor Server')
        data_enc = conn.recv(2048)
        print('Received Encrypted Data from Sensor Server')
        data = rsa.decrypt(data_enc,priv_ser_1)
        D1 = pickle.loads(data)
        data_enc = conn.recv(2048)
        data = rsa.decrypt(data_enc,priv_ser_1)
        D2 = pickle.loads(data)

        D = {**D1, **D2}

        for i in field_names:
            t = pickle.dumps(D[i])
            t_enc = rsa.encrypt(t, priv_master)
            D[i] = t_enc.hex()
        print('Encrypted data to be stored in Logs')
        print(D)

        with open('/home/ubuntu/Logs/logs.csv','a') as f_object:
            dictw_obj = DictWriter(f_object, fieldnames = field_names)
            dictw_obj.writerow(D)
            f_object.close()
        print('Logs Written')
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
        l = pickle.loads(conn.recv(512))
        print(f"Connected by {addr}")
        for m in range(l):
            pub_ser_2,priv_ser_2 = rsa.newkeys(1024)
            conn.sendall(pickle.dumps(pub_ser_2))
            print('Sent Main Server Public Key', (m+1))
            pub_act_b = conn.recv(1024)
            print('Received Actuator Server Public Key', (m+1))
            pub_act = pickle.loads(pub_act_b)
            data_b = conn.recv(1024)
            print('Received Encrypted Request for Data')
            data = rsa.decrypt(data_b,priv_ser_2)
            print('Request:', data)
            [param,i] = data.decode('UTF-8').split(',')
            i = int(i)
            (abs_val, avg_val) = (0,0)
            if param == 'smoke':
                log_data = Logs_Data['smoke_i'].tolist()
                (abs_val) = reading(i,log_data)
            elif param == 'dis':
                log_data = Logs_Data['dis_i'].tolist()
                (abs_val) = reading(i,log_data)
            elif param == 'dep':
                log_data = Logs_Data['dep_i'].tolist()
                (abs_val) = reading(i,log_data)
            elif param == 'temp':
                log_data = Logs_Data['temp_i'].tolist()
                (abs_val) = reading(i,log_data)
            elif param == 'hum':
                log_data = Logs_Data['hum_i'].tolist()
                (abs_val) = reading(i,log_data)
            elif param == 'light':
                log_data = Logs_Data['light_i'].tolist()
                (abs_val) = reading(i,log_data)
            else:
                continue
            sending_data = {'Parameter':param, 'abs_val':abs_val}
            sending_data_encoded = pickle.dumps(sending_data)
            sending_data_enc = rsa.encrypt(sending_data_encoded, pub_act)
            conn.sendall(sending_data_enc)
            print("Sent Encrypted Data")
        conn.close()
        try:
            conn.sendall(b'ping')
            print('Still open')
        except:
            print('Connection Closed')
        
        time.sleep(2)
