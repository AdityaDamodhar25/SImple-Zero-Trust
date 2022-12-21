from csv import writer
from csv import DictWriter
from pandas import *
import socket
import hashlib
import rsa
import pickle
import time

(priv_master, pub_master) = rsa.newkeys(512)

field_names = ['dis_i','temp_i']

with open('/home/ubuntu/Logs/logs.csv','w') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(field_names)
    f_object.close

HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
PORT_S = 65432  # Port to listen on (non-privileged ports are > 1023)
PORT_A = 54321


def reading(ind,log_data):
    ind_ = ind-1
    abs_val_enc = bytes.fromhex(log_data[ind_])
    abs_val = pickle.loads(rsa.decrypt(abs_val_enc, pub_master))
    return (abs_val)



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
        print('Shared Public key to Sensor Server')
        data_enc = conn.recv(2048)
        print('Received Data from Sensor Server')
        data = rsa.decrypt(data_enc,priv_ser_1)
        D = pickle.loads(data)

        for i in field_names:
            t = pickle.dumps(D[i])
            t_enc = rsa.encrypt(t, priv_master)
            D[i] = t_enc.hex()

        print('Encrypted data for storage:')
        print(D)

        with open('/home/ubuntu/Logs/logs.csv','a') as f_object:
            dictw_obj = DictWriter(f_object, fieldnames = field_names)
            dictw_obj.writerow(D)
            f_object.close()
        print("Data stored in Logs")
        conn.close()
        try:
            conn.sendall(b'ping')
            print('Still open')
        except:
            print('Closed')

    time.sleep(2)

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
        l = len(field_names)
        for i in range(l):
            pub_ser_2,priv_ser_2 = rsa.newkeys(1024)
            pub_ser_2_b = pickle.dumps(pub_ser_2)
            conn.sendall(pub_ser_2_b)
            print('Shared Public Key',(i+1),'to Actuator Server')
            pub_act_b = conn.recv(1024)
            print('Received Public key', (i+1),'from Actuator Server')
            pub_act = pickle.loads(pub_act_b)
            data_b = conn.recv(1024)
            data = rsa.decrypt(data_b,priv_ser_2).decode()
            print('Received and decoded data')
            [param,index] = data.split(',')
            index = int(index)
            (abs_val, avg_val) = (0,0)
            col = field_names[i]
            log_data = Logs_Data[col].tolist()
            abs_val = reading(index,log_data)
            sending_data = {'Parameter':param, 'abs_val':abs_val}
            sending_data_encoded = pickle.dumps(sending_data)
            sending_data_enc = rsa.encrypt(sending_data_encoded, pub_act)
            conn.sendall(sending_data_enc)
            print("Sent Requested Data after Encryption")
        conn.close()
        try:
            conn.sendall(b'ping')
            print('Still open')
        except:
            print('Closed')
        
        time.sleep(5)
