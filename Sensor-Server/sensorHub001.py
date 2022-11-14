from pandas import *
import time
import random
import socket
import json


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

	i = random.randint(0,ls)
	return smoke[i]

def dist_sensor(ldis):

	i = random.randint(0,ldis)
	return dist[i]

def depth_sensor(ld,idep):

	i = idep + random.randint(-3,3)
	if (i>=ld or i<0):
		i = idep
	return (depth[i],i)

def temp_sensor(lt,itemp):

	i = itemp + random.randint(-3,3)
	if (i>=lt or i<0):
		i = itemp
	return (temp[i],i)

def hum_sensor(lh,ihum):

	i = ihum + random.randint(-3,3)
	if (i>=lh or i<0):
		i = ihum
	return (hum[i],i)

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

	return (light[i], i, cl)



ls = len(smoke)
ldis = len(dist)
ld = len(depth)
lt = len(temp)
lh = len(hum)
ll = len(light)

HOST = "13.231.119.83"
PORT = 65432

smoke_val = smoke_sensor(ls)
dis_val = dist_sensor(ldis)

idep = random.randint(0,(ld-1))
dep_val = depth[idep]

itemp = random.randint(0,(lt-1))
temp_val = temp[itemp]

ihum = random.randint(0,(lh-1))
hum_val = hum[ihum]

il = random.randint(0,(ll-1))
light_val = light[il]
cl = 2
while(True):

	D = {'smoke_i':smoke_val, 'dis_i':dis_val, 'dep_i':dep_val, 'temp_i':temp_val, 'hum_i':hum_val, 'light_i':light_val}
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		sending_data = json.dumps(D).encode('utf-8')
		s.sendall(sending_data)
		data = s.recv(1024)
	print(f"Received {data!r}")

	print('Smoke Value:', smoke_val)
	print('Distance Value:', dis_val)
	print('Depth Value:', dep_val)
	print('Temperature Value:', temp_val)
	print('Humidity Value:', hum_val)
	print('Light Value:', light_val)
	print()

	time.sleep(5)

	smoke_val = smoke_sensor(ls)
	dis_val = dist_sensor(ld)
	(dep_val,idep) = depth_sensor(ld, idep)
	(temp_val,itemp) = temp_sensor(lt, itemp)
	(hum_val,ihum) = hum_sensor(lh, ihum)
	(ligth_val, il, cl) = light_sensor(ll, il, cl)


