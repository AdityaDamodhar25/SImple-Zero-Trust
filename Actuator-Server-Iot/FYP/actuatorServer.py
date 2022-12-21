import socket
import pickle
import time
import rsa
import hashlib
import gpiozero
import time
import RPi.GPIO as GPIO


print('Resetting Servo controlling Cooling-Intensity')
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization
p.ChangeDutyCycle(5)
time.sleep(0.5)
p.ChangeDutyCycle(7.5)
time.sleep(0.5)
p.ChangeDutyCycle(10)
time.sleep(0.5)
p.ChangeDutyCycle(12.5)
time.sleep(0.5)
p.ChangeDutyCycle(10)
time.sleep(0.5)
p.ChangeDutyCycle(7.5)
time.sleep(0.5)
p.ChangeDutyCycle(5)
time.sleep(0.5)
p.ChangeDutyCycle(2.5)
time.sleep(0.5)

def dis_func(x):

    if (x>=15):
        led = gpiozero.LED(15)
        buzzer = gpiozero.Buzzer(3)
        buzzer.on()
        led.on()
        time.sleep(2)
        buzzer.off()
        led.off()
    else:
        led = gpiozero.LED(14)
        led.on()
        time.sleep(2)
        led.off()



def temp_servo(temp_val):
    dc = (temp_val*0.2)+2.5
    p.ChangeDutyCycle(dc)



HOST = "43.207.32.202" 
PORT = 54321


func_names = ['dis_i','temp_i']
i = 0
index = 1
l = len(func_names)

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
    for i in range(l):    
        pub_act, priv_act = rsa.newkeys(1024)
        pub_ser_2_b = s.recv(1024)
        print('Received Public key', (i+1), 'of Main Server')
        pub_ser_2 = pickle.loads(pub_ser_2_b)
        s.sendall(pickle.dumps(pub_act))
        print('Shared Public Key', (i+1), 'of Actuator Server')
        text = func_names[i]
        sending_text = text+','+str(index)
        sending_data = sending_text.encode('UTF-8')
        sending_data_enc = rsa.encrypt(sending_data, pub_ser_2)
        s.sendall(sending_data_enc)
        print('Encrypted Request for', func_names[i] ,'Data sent')
        data_enc = s.recv(1024)
        print('Received Encrypted', func_names[i], 'Data')
        data = rsa.decrypt(data_enc, priv_act)
        D = pickle.loads(data)
        print(f"Received {D}")
        if (i == 0):
            d = D['abs_val'] 
            dis_func(d)
            print('Status of egg availability alerted')
        elif (i == 1):
            print('Cooling-Intensity altered according to ambient temperature inside Fridge')
            temp_val = D['abs_val']
            temp_servo(temp_val)
        else:
            print('Error')
    index += 1
    s.close()
    try:
        s.sendall(b'ping')
        print('Connection open')
    except:
        print('Connection closed')
    time.sleep(3)


