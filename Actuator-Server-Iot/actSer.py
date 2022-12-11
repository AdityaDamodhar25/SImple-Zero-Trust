import socket
import pickle
import time
import rsa
import hashlib
import gpiozero
import time


def buzz():
    buzzer = gpiozero.Buzzer(3)
    buzzer.on()
    time.sleep(2)
    buzzer. off()


HOST = "43.207.32.202" 
PORT = 54321


func_names = ['dis']
i = 0
index = 1

print('------------------------')
print('----Actuator Server----')
print('------------------------')

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    go = s.recv(1024)
    print('Received {go}')
    password = b'12345'
    pass_hash = hashlib.sha256(password).hexdigest()
    s.sendall(pass_hash.encode())
    data = s.recv(1024)
    instruction = data.decode('utf-8')
    if (instruction != 'go'):
        print('Incorrect passkey, Authentication Failed. Connection closed')
        s.close()
        try:
            s.sendall(b'ping')
            print('Incorrect working, connection still open')
        except:
            print('Correct Working, connection closed')
        continue
    else:
        print('Accurate passkey, Autheticated')
    pub_act, priv_act = rsa.newkeys(1024)
    pub_ser_2_b = s.recv(1024)
    pub_ser_2 = pickle.loads(pub_ser_2_b)
    s.sendall(pickle.dumps(pub_act))
    text = func_names[i]
    sending_text = text+','+str(index)
    sending_data = sending_text.encode('UTF-8')
    sending_data_enc = rsa.encrypt(sending_data, pub_ser_2)
    s.sendall(sending_data_enc)
    data_enc = s.recv(1024)
    print('Received Data')
    data = rsa.decrypt(data_enc, priv_act)
    D = pickle.loads(data)
    print(f"Received {D}")
    index += 1
    s.close()
    d = D['abs_val'] 
    if(d>=17):
        buzz()
    try:
        s.sendall(b'ping')
        print('Connection open')
    except:
        print('Connection closed')
    time.sleep(3)




