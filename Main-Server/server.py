from csv import writer
from csv import DictWriter
import socket
import hashlib
import rsa
import pyaes
import secrets
import pickle

HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

field_names = ['smoke_i', 'dis_i', 'dep_i', 'temp_i', 'hum_i', 'light_i']



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

while(True):
    s.listen()
    conn, addr = s.accept()
    with conn:
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
