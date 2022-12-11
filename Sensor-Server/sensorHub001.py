from pandas import *
import time
import random
import socket
import hashlib
import rsa
import pickle



Water_Level = read_csv("/home/ubuntu/WaterLevel.csv")
Smoke_Level = read_csv("/home/ubuntu/Smoke.csv")
Distance_Level = read_csv("/home/ubuntu/Ultrasonic.csv")
Temp_Level = read_csv("/home/ubuntu/Temperature.csv")
Hum_Level = read_csv("/home/ubuntu/Humidity.csv")
Light_Level = read_csv("/home/ubuntu/Light.csv")

depth = Water_Level['Water Depth/WaterLevel001.Average'].tolist()
depth.sort()

smoke = Smoke_Level['Smoke.Average'].tolist()
smoke.sort()

dist = Distance_Level['Distance.Average'].tolist()
dist.sort()

temp = Temp_Level['Temperature.Average'].tolist()
temp.sort()

hum = Hum_Level['Humidity.Average'].tolist()
hum.sort()

light = Light_Level['Ambient light/Light_Sensor_001.Average'].tolist()
light.sort()

def smoke_sensor(ls):

    i = random.randint(0,(ls-1))
    return round(smoke[i],5)

def dist_sensor(ldis):

    i = random.randint(0,(ldis-1))
    return round(dist[i],5)

def depth_sensor(ld,idep):

    i = idep + random.randint(-3,3)
    if (i>=ld or i<0):
        i = idep
    return (round(depth[i],5),i)

def temp_sensor(lt,itemp):

    i = itemp + random.randint(-3,3)
    if (i>=lt or i<0):
        i = itemp
    return (round(temp[i],5),i)

def hum_sensor(lh,ihum):

    i = ihum + random.randint(-3,3)
    if (i>=lh or i<0):
        i = ihum
    return (round(hum[i],5),i)

def light_sensor(ll,il,cl):

    if cl<=240:
        i = il + random.randint(-2,2)

    elif cl<=360:
        i = il + random.randint(-3,0)

    elif cl<=600:
        i = il + random.randint(-2,2)

    elif cl<= 720:
        i = il + random.randint(0,3)

    else:
        cl = cl%720

    cl+=1
    if(i>=ll or i<0):
        i = il
    ret_val = round(light[i],5)
    return (ret_val, i, cl)



ls = len(smoke)
ldis = len(dist)
ld = len(depth)
lt = len(temp)
lh = len(hum)
ll = len(light)

HOST = "43.207.32.202" 
PORT = 65432    

smoke_val = smoke_sensor(ls)
dis_val = round( dist_sensor(ldis),5)

idep = random.randint(0,(ld-1))
dep_val = round(depth[idep],5)

itemp = random.randint(0,(lt-1))
temp_val = round(temp[itemp],5)

ihum = random.randint(0,(lh-1))
hum_val = round(hum[ihum],5)

il = random.randint(0,(ll-1))
light_val = round(light[il],5)
cl = 2
while(True):

    D1 = {'smoke_i':smoke_val, 'dis_i':dis_val, 'dep_i':dep_val}
    D2 = {'temp_i':temp_val, 'hum_i':hum_val, 'light_i':light_val}
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    go = s.recv(1024)
    print(f'Received {go}')
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
    sending_data = pickle.dumps(D1)
    print(len(sending_data))
    pub_ser_b1 = s.recv(2048)
    pub_ser_1 = pickle.loads(pub_ser_b1)
    encrypted = rsa.encrypt(sending_data, pub_ser_1)
    s.sendall(encrypted)
    sending_data = pickle.dumps(D2)
    print(len(sending_data))
    encrypted = rsa.encrypt(sending_data, pub_ser_1)
    s.sendall(encrypted)


    print('Sent Data')

    smoke_val = smoke_sensor(ls)
    dis_val = dist_sensor(ld)
    (dep_val,idep) = depth_sensor(ld, idep)
    (temp_val,itemp) = temp_sensor(lt, itemp)
    (hum_val,ihum) = hum_sensor(lh, ihum)
    light_ret_val = light_sensor(ll, il, cl)
    light_val = light_ret_val[0]
    il = light_ret_val[1]
    cl = light_ret_val[2]
    s.close()
    try:
        s.sendall(b"ping")
        print("Connection open")
    except:
        print("Connection closed")

