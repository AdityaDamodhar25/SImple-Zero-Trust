from pandas import *
import time
import random
import socket
import hashlib
import rsa
import pickle


import RPi.GPIO as GPIO

def dis():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    TRIG = 11
    ECHO = 12
    print("Distance Measurement In Progress")
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.output(TRIG, False)
    print("Waiting For Sensor To Settle")
    time.sleep(2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end-pulse_start
    distance = pulse_duration*17150
    distance = round (distance, 2)
    print("Distance:", distance, "cm")
    return distance





HOST = "43.207.32.202" 
PORT = 65432    

print('------------------------------')
print('--------Sensor Server--------')
print('------------------------------')

while(True):

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
    dist = dis()
    D1 = {'dis_i':dist}
    sending_data = pickle.dumps(D1)
    pub_ser_b1 = s.recv(2048)
    pub_ser_1 = pickle.loads(pub_ser_b1)
    encrypted = rsa.encrypt(sending_data, pub_ser_1)
    s.sendall(encrypted)
   
    print('Sent Data')

    s.close()
    try:
        s.sendall(b"ping")
        print("Connection open")
    except:
        print("Connection closed")

