# SImple-Zero-Trust

### ABSTRACT:

The Internet of Things (IoT) is one of the novel concepts which has taken the world by storm. The ability to integrate regular home appliances on the internet allowing remote access from anywhere has been progressing rapidly. Although the technology holds many advantages, the security concerns in these systems make them double-edged swords. Zero-Trust has been introduced in the security industry as the answer to most cyber threats present. The segmentation of access rights, even within internal nodes of the system is a key feature of this model.
Our project titled “Trust-Free Homes: An Analysis of Performance and Scalability of the Zero-Trust paradigm in Smart Home systems”, aims at implementing a Zero - Trust System to analyse its capabilities in IoT networks. The limited capabilities of IoT devices makes running multiple key-generation algorithms, and key-storage a point of concern, and implementing Zero-Trust without affecting their regular functioning at scale is a challenge. The project will be carried out by simulating the behaviour of IoT devices using Azure’s simulation capabilities for modelling the network, then using Python for implementing a working system on a very small IoT network.
The efficiency of the implemented Zero-Trust network will be scrutinised, and possible improvements to implementations will be tried. This project is aimed at serving as a guide to a working model of the Zero-Trust guidelines.

### CONTENTS

1. [INTRODUCTION](### 1. INTRODUCTION:)
     1. [OBJECTIVES](##### 1.1. OBJECTIVES:)
2. LITERATURE SURVEY
3. ZERO TRUST PARADIGM
4. METHODOLOGY
     1. SIMULATED IoT NETWORK
        1. Sensor Server
        2. Main Server
        3. Actuator Server
     2. ZERO-TRUST IMPLEMENTATION
     3. PHYSICAL IoT IMPLEMENTATION
     4. DEMONSTRATING SECURITY
5. CONCLUSION
     1. .[FUTURE SCOPE](###5.1-FUTURE SCOPE:)
.[REFERENCES](###REFERENCES:)

### 1. INTRODUCTION:
Internet-of-Things (IoT) is one the key concepts leading into Industry 4.0. It is the integration of all devices over a single network, effectively communicating to one another, setting up a continuous stream of data allowing all devices on the network to access the same for effective decision-making, thus improving the state-of-art of industries. All this data is freely accessible and is stored on low-power, limited capability IoT devices, thus severely crippling the security for the same. The state of the cyber-landscape is such that the more integrated and exposed a system is, the easier it is for malicious actors to exploit the same. IoT is particularly at risk, due to low grade of security in IoT devices. 

Among the many methods proposed and used in the industry to secure the same, the Zero-Trust Paradigm is a promising new idea. Its novelty lies in the fact that unlike traditional perimeter-based methods, Zero-Trust preaches complete isolation and segmentation, even within a network. It aims to secure all data and functionality of the network and its nodes by verifying and encrypting all data and communications, as well as granting only required privileges post authentication on-demand.

Zero-Trust functions on the motto, “Never Trust, Always Verify”. This policy of segmentation and verification safeguards sensitive data from the threat of compromised internal nodes. The segmentation localises the compromise to a specific area, following which the Intrusion Detection and Prevention System (IDPS) notifies the administrator about the security breach and takes further preventive measures to stop the leakage of data.

Zero-Trust has an edge over perimeter based security because of the human factor in security breaches. Weak passwords, unchanged router or server default passwords, accidental introduction of malware into internal nodes are all possible with human intervention. Unfortunately, human intervention is also required for smooth functioning of many networks, as well as the repair and recovery of many compromised networks. Thus, setting external perimeters alone compromises the overall security of the network, due to high risk of compromise of an internal node, within the perimeter.

Despite the obvious advantages in adopting Zero-Trust, it still is an idea, and there is no codification in guidelines of adoption. There are multiple implementations by multiple organisations, each tailoring the guidelines to match their requirements. The lack of standardisation, combined with the need for investment in changing the landscape of the internal network have been major detriments to the adoption of this paradigm.

##### 1.1. OBJECTIVES:
This work has the following objectives:
- Simulate an IoT network by building everything from the basic connections and implementing a basic security model in accordance to the Zero-Trust principles.
- Verify the adaptability of the security model by deploying it in a similar IoT network.
- Demonstrate security of the implemented security model.

The report is structured as follows: the literature considered and their key points are first described, post which there is a detailed explanation of Zero-Trust model, followed by the methodology adopted by the project. Prior to the design of the Zero-Trust model, an IoT network is simulated and the architecture and working is explained. This is followed by the description of the implemented Zero-Trust model, and the explanation of what principles each change satisfies. This is followed by the description of the physical IoT network built to match the architecture of the simulated IoT network, and illustrates the deployment of the Zero-Trust model in the same. This is finally followed by an illustration of capabilities of a malicious agent, who is assumed to have compromised and escalated privileges in one of the IoT devices.

### 2. LITERATURE SURVEY:

In the article by Buck et al [1], the authors provide an overview on the current trends and research interests in the field of Zero-Trust security. Equal importance is given to grey literature as well, apart from academic literature due to the pioneering work in implementations done by the industry.

Kindervag [3] in his pioneering work on Zero-Trust illustrates the prime focus of a Zero-Trust network architecture. The work differentiates the traditional architecture where security is an overlay from the Zero-Trust architecture envisioned in 2010, where security is an integral component of the very core of the architecture. 

Friedman’s [2] work provides detailed insight into the Zero-Trust paradigm. It cohesively explains the failure of the promise of traditional security, followed by the promise of Zero-Trust. It further elaborates on the security landscape, describes methods to define and protect different zones on the landscape, each of a different level of required security.
 
In the IEEE paper by Palmo et al [5], the authors provide insight into a Software-Defined Perimeters (SDP), a security model built with Zero-Trust in mind. They outlined the disadvantages of existing SDN models and proposed scalable SDN architectures which satisfy modern network requirements.

The article by Mahajan et al. [4] provides insight into basics of IoT, and the necessary description of the simple IoT network envisioned for this project. It describes the components required and working for an IoT based Smart Refrigerator, and the methodology used for the working of the same. We have taken inspiration from the same to build the physical IoT network on which the constructed Zero-Trust model is deployed.

### 3. THE ZERO-TRUST PARADIGM

All traditional security models are based on trust. Some networks are trusted, some users are trusted and some devices are trusted. This trust boundary is established by very stringent firewalls, rigorous whitelisting of data and constant monitoring of all incoming and outgoing data. This security model has been relatively successful, barring one special case of malicious actors, i.e. the malicious insider. This is the scenario where a user, device or network classified as “trusted” acts as the source of malicious activity. In this case, the basic premise of the security system fails, and the malicious agent wrecks havoc on the network. 

Improving security comes as a result of changing the model of trust. Zero-Trust model is a proposition that does the same. It applies the same conditions and regulations it does to a node from an internal system that it does to a node from an external system.  This means encryption, verification and authentication of all devices, as well as providing access to network resources and data on a need-only basis. Zero-Trust does not mean not to trust the employees of an organisation, rather it applies to the data and communications being transferred around in the network of the organisation.

One of the advantages of the Zero-Trust model is that it is platform agnostic. The same principles can be applied to all platforms and networks, achieving the expected result. It is also highly scalable, for the newer segments of the network can be integrated along with older segments effectively. It can effectively replace an existing system, as the architecture of the Zero-Trust system is inside-out, i.e. smaller segments are completely secured prior to integrating all segments together. Once the segments are integrated, the connections between segments are secured as well.
It must be noted that the smaller components of security, namely firewalls, VPNs, whitelists, access control mechanisms, intrusion prevention systems, cryptography, etc. are not obsolete in this model, rather their method of deployment is altered. They are used extensively in the boundaries between segments, for encrypting all communications of the network, and to provide access to resources on the need-only basis. Apart from all this, all data is logged and stored for future reference.

![Sample Zero Trust Process Flowchart](https://user-images.githubusercontent.com/66631868/209555723-ef844b8c-a620-4c2f-8a6c-da4791e40c6f.png)

_Figure 1: Zero - Trust Process Flowchart_

### 4. METHODOLOGY:

Keeping in mind principles of Zero-Trust, an IoT network is simulated, and then zero-trust security is implemented. Post implementation, an actual IoT set-up is constructed and the zero-trust is translated into this physical network. A home automation network is simulated because of simplicity in the types of sensors used, and intuitive knowledge of data that has to be processed. 

![Architecture of IoT Network system](https://user-images.githubusercontent.com/66631868/209577665-06602422-aca6-4199-97c4-abd62987eac2.png)

_Figure 2: Architecture of IoT Network system._

##### 4.1 SIMULATED IOT NETWORK:

This IoT network becomes the testing ground to deploy the Zero-Trust model. The architecture of this network is designed keeping the aspects of segmentation and localization in mind. Home automation systems are generally controlled by a central server, either set locally, or in the cloud. All sensors collect and send their data to this server, logs the data and communications, and takes a decision based off the same. It then instructs the actuators to perform necessary actions.

This traditional architecture believes that all nodes on the network, i.e. the sensors and actuators are trusted. Thus, compromise of the internet module of these devices exposes the main server to attack, thus resulting in the loss of personal data. Thus, while implementing the Zero-Trust network architecture, this work segments the functions of the main server into three smaller servers so as to minimise risk associated with usage of vulnerable IoT devices.


![List of Sensors Simulated in Azure IoT Central](https://user-images.githubusercontent.com/66631868/209577752-4696b1df-3219-4ae4-92f4-1f79ec537812.png) 

_Figure 3: List of Sensors Simulated in Azure IoT Central._ 

This smart home system segments the main server generally used by other smart-home systems. It divides the single server into three, namely main server, sensor server and actuator server. The sensor server performs the job of collecting data from the sensors and sending it to the main server. It also maintains information about the health of the sensors. The actuator server acts as the point-of-contact between the main server and any deployed actuator. This server keeps track of the status and health of actuators as well. The main server acts as the mediator between the other two servers, while performing the function of logging.
This design keeps in mind the ideas of Zero_Trust, thus segmenting and localising risk. The points of vulnerability are known to be the IoT devices, and may even extend to locally deployed server nodes. Thus, the damage is localised to only either the sensors or the actuators when there is a compromise in any of the above. In this case, the main server and the logged data are totally isolated from the region of compromise. 

All servers are simulated on Amazon Web Services Elastic Compute Cloud (EC2 instances). Python3 is the primary choice of programming language, and Socket programming is used for all communications. This is due to the low-level control offered by sockets, which is helpful to customise the network to match our security requirements. The data for the IoT network to run on is simulated using Azure IoT Central, which generates telemetry based on device templates defined by the user.

###### 4.1.1 SENSOR SERVER:

The sensor server as described above has the function of collecting data from the sensors and presenting it to the main server. The data to be collected in this simulation was generated prior from Microsoft Azure’s IoT Central, and stored as .csv files in the sensor server. It is then retrieved and sent to the main server when required.

![Devices defined in Azure ioT Central](https://user-images.githubusercontent.com/66631868/209817776-be527be6-f254-436d-8ee9-d15b1b347e81.png)

_Figure 4: Devices defined in Azure IoT Central_

![Device templates defined in Azure IoT Central](https://user-images.githubusercontent.com/66631868/209817957-22c0dae1-a777-4c43-913d-37e048d524da.png)

_Figure 5: Device templates defined in Azure IoT Central_

![Simulated data from Azure IoT Central](https://user-images.githubusercontent.com/66631868/209818154-bd14298b-e4cb-47c2-8c6e-d56833ffbeb8.png)

_Figure 6: Simulated data from Azure IoT Central._

![Sensor server on AWS with data as csv files](https://user-images.githubusercontent.com/66631868/209818444-d6f96e57-73d8-4bd1-8fc1-1a71e0dadca4.png)

_Figure 7: Sensor server on AWS with data as .csv files_

###### 4.1.2 MAIN SERVER:

This server is the central portion of the network, acting as an interface for all communications. Despite its control role, it does not make any decisions regarding actuation, rather provides the actuator server the data necessary to make the same decisions. It must be noted that, this server refrains from sending any sensitive data to the sensor server, and sends data from logs to the actuator server only when an authenticated request arrives, and even then, the data required for the current computation is only shared.

![Main Server](https://user-images.githubusercontent.com/66631868/209818645-ba758b33-36ee-4f01-9ee8-43e28cdb5113.png)

_Figure 8: Main Server_

![Logging being done on the Main Server](https://user-images.githubusercontent.com/66631868/209818821-efb6523f-cbf1-469c-93f3-587ed6434a5f.png)

_Figure 9: Logging being done on the Main Server._

###### 4.1.3 ACTUATOR SERVER:

This server connects directly to the deployed actuators, and acts as the means to communicate to the same. Actuator server gets data it specifically requests for from the main server and computes the conditions to be matched for specific actuation. 

![Actuator server](https://user-images.githubusercontent.com/66631868/209819374-112d8263-1cab-4a87-b27f-5c17d3ef3a31.png)

_Figure 10: Actuator server_

##### 4.2 ZERO-TRUST IMPLEMENTATION:

![Workflow Diagram](https://user-images.githubusercontent.com/66631868/209819584-7349fad9-1f72-4af1-a6e3-83b5c1e2c782.png)

_Figure 11: Workflow Diagram_

The architecture of this system has Zero-Trust in mind, and the segmentation and localization aspect of the Zero-Trust requirements are satisfied. This allows us to concentrate on securing communication and data storage, with proper authentication mechanisms in place. 

On the sensor server, the data from Azure IoT Central is not encrypted, as it is assumed to be real-time data gathered just before sending data to the main server. Prior to all communication, the sensor server has to authenticate itself by sharing the sha-256 hash of a pre-shared key. On the main server, this hash is locally computed and compared, and communications proceed only if there is a match. Else, the socket is closed and the connection is terminated. Communications with the main server are encrypted with the RSA algorithm, and for each communication, a new set of keys are generated by the main-server and the public key is sent to the sensor server. The sensor server encrypts the data to be sent using the public key of the main server, thus ensuring secrecy.

![Sensor Server Message](https://user-images.githubusercontent.com/66631868/209819721-8a54303c-ab10-4f36-9689-b3ab21f72e5a.png)

_Figure 12: Sensor Server Messages_

The main server stores all received data in an encrypted format, using AES cipher for security purposes. It then decrypts the data and sends only the requested data to the actuator server. The actuator server also has a similar authentication mechanism to the sensor server, using the sha-256 hash of a pre-shared password. Then as the communications between the actuator server and main server are bidirectional (works on a request-response basis), two sets of RSA keys are generated, one on each server. The public keys are shared to each other for securing the communication. It must be noted that as the keys are regenerated for each round of messages, both with the sensory server and actuator server, the risk of cryptanalytic attacks on the RSA encryption is minimised.

![Main Server Messages](https://user-images.githubusercontent.com/66631868/209819813-0f1a0676-c3fb-47de-a3e3-5e50473ce574.png)

_Figure 13: Main Server Messages_

![Actuator Server Messages](https://user-images.githubusercontent.com/66631868/209819900-bc63d486-2049-4d5a-aa7b-87efe4ad9586.png)

_Figure 14: Actuator Server Messages_

##### 4.3 PHYSICAL IoT IMPLEMENTATION:

The principles and concepts applied to the above Simulated network are followed and a physical IoT network is implemented. It is inspired from the implementation of a smart refrigerator from Mahajan et al., and contains a temperature sensor to sense ambient temperature inside the fridge and an ultrasound sensor to detect distance to the closest body, used to check for the number of eggs present. For actuation, based on the received data, a servo motor is implemented to change the intensity of cooling, and there are LEDs which are used to alert the user periodically about the status of eggs’ availability.

![Developed Real Time IoT Network](https://user-images.githubusercontent.com/66631868/209820067-5216212f-69ce-478f-bd3e-6346201995a3.png)

_Figure 15: Developed Real Time IoT Network_

The Sensor Server is implemented using a Raspberry pi 4, with the ultrasonic sensor HC-SR04 and temperature sensor DHT-11 interfaced via the GPIO pins. DHT-11 can also measure atmospheric humidity, but the project neglects that functionality. The Main Server is still implemented on the cloud, i.e. the AWS Electronic Compute Cloud (EC2) instance is used. It functions similar to the initial functioning of the Main Server instance, only changing the number of data types it stores. The Actuator Server is also deployed on a Raspberry pi 4, with a Servo motor and LEDs and Buzzer interfaced via the GPIO pins. 

![Main server messages](https://user-images.githubusercontent.com/66631868/209839113-bc6ee445-cbd2-44b1-91c0-dbc80b119083.png)

_Figure 16: Main Server Message_

![Sensor Server Message](https://user-images.githubusercontent.com/66631868/209839576-60e54efd-9875-4a74-976f-20695cb9ef2b.png)

_Figure 17: Sensor Server Initial Message_

![Actuator Server First Message](https://user-images.githubusercontent.com/66631868/209840303-186a719f-23fc-41f3-95b0-004ded8603e7.png)

_Figure 18: Actuator Server Initial Message_

The LEDs and Buzzer are set to alert the status of egg availability periodically, with a flash of green LED when the closest egg to the sensor is within a threshold (say 15 cm), and the flashing of red LED and a Buzzer sound when the closest egg to the sensor is beyond the threshold. The user is assumed to remove eggs closest to the sensor first in order for the demo model to work. The demo is performed by placing an obstacle at different distances from the sensor and observing the LED alerts.

![Distance within threshold](https://user-images.githubusercontent.com/66631868/209840407-f3b64f70-bb36-4760-a4ca-fbe2f6adb6af.jpeg)

_Figure 19: Object within Threshold, Green LED_

![Sensor Server Distance 1](https://user-images.githubusercontent.com/66631868/209848215-92d58972-03a4-43a4-9d94-88b1c63e1af7.png)

_Figure 20: Sensor Server Functioning for Object within Threshold_

![Actuator Server Distance 1](https://user-images.githubusercontent.com/66631868/209848314-af24d8b6-5d96-48cc-8e31-583f46ab722c.png)

_Figure 21: Actuator Server Functioning for object within Threshold_

![Distance Beyond Threshold](https://user-images.githubusercontent.com/66631868/209848365-e814725a-51fa-44ce-8880-218d802f7ca4.jpeg)

_Figure 22: Object beyond Threshold, Red LED_

![Sensor Server Distance 2](https://user-images.githubusercontent.com/66631868/209848451-f43a2c00-01f1-4d2d-af94-946927cd52c0.png)

_Figure 23: Sensor Server Functioning for Object beyond Threshold_

![Actuator Server Distance 2](https://user-images.githubusercontent.com/66631868/209848512-49777673-8988-4b92-80d0-086be3e65197.png)

_Figure 24: Actuator Server Functioning for object beyond Threshold_

At the start of the system, the Servo motor is set to minimum Cooling Intensity configuration, and is changed to higher levels as the ambient temperature data is received. When any new bodies with higher temperature are introduced to the cooling chamber, the ambient temperature varies, which is read by the DHT-11. This data when received by the Actuator Server changes the configuration of the Servo motor to increase Cooling-Intensity accordingly.

![Initial Configuration](https://user-images.githubusercontent.com/66631868/209848628-c0dd191f-3fc4-420a-84ed-ab4259d2cb2b.jpeg)

_Figure 25: Initial Configuration of Servo_

![Heating](https://user-images.githubusercontent.com/66631868/209848723-8c32e30f-066a-44e5-ab7a-96a803e9b867.jpeg)

_Figure 26: Using Hot Metal Water Bottle to increase Ambient Temperature_

![Sensor Server Temperature increase 1](https://user-images.githubusercontent.com/66631868/209848800-4bf7bedf-3818-46d5-9624-62154a6de099.png)

_Figure 27: First Rise in Temperature Read by Sensor Server_

![Actuator Server Temperature increase 1](https://user-images.githubusercontent.com/66631868/209848862-8cfcfd93-fe6a-4d57-85ae-be4b2bab944c.png)

_Figure 28: First Rise in Temperature processed by Actuator Server_

![Temperature Increase 1](https://user-images.githubusercontent.com/66631868/209848913-530c4344-8d34-4166-b5ba-5a43c847adda.jpeg)

_Figure 29: First Adjustment by Servo Motor_

![Sensor Server Temperature increase 2](https://user-images.githubusercontent.com/66631868/209848987-eb031315-06ef-493a-ad08-2f1ecb438a58.png)

_Figure 30: Second Rise in Temperature Read by Sensor Server_

![Actuator Server Temperature increase 2](https://user-images.githubusercontent.com/66631868/209849108-6ac32942-de6d-494a-a827-0decf58d66f0.png)

_Figure 31: Second Rise in Temperature processed by Actuator Server_

![Temperature increase 2](https://user-images.githubusercontent.com/66631868/209849224-c8a4001f-73de-4233-91f9-27b0447fe5a4.jpeg)

_Figure 32: Second Adjustment by Servo Motor_

![Sensor Server Temperature increase 3](https://user-images.githubusercontent.com/66631868/209849220-82c46562-0d83-4754-842f-d052e5220caa.png)

_Figure 33: Third Rise in Temperature Read by Sensor Server_

![Actuator Server Temperature increase 3](https://user-images.githubusercontent.com/66631868/209849189-7d645b79-3867-4bac-9d48-f81f07107ef9.png)

_Figure 34: Third Rise in Temperature processed by Actuator Server_

![Temperature increase 3](https://user-images.githubusercontent.com/66631868/209849229-3bc839d1-63a8-4e5c-8d9b-47c47b0dce52.jpeg)

_Figure 35: Third Adjustment by Servo Motor_

The Main Server encrypts all data using the RSA algorithm, and stores all the data as Hexadecimal values in the logs, thus ensuring secrecy in the event of a compromise in the security of the Main Server. The Logs of encrypted data are illustrated below in Figure 33.

![Encrypted Logs](https://user-images.githubusercontent.com/66631868/209849199-969eee0a-7d9a-4be6-b97e-3a1b9292ef6e.png)

_Figure 36: Encrypted Logs on Main Server_

##### 4.4 DEMONSTRATING SECURITY:

This project is an attempt at using the Zero-Trust ideology to secure an IoT network, thus security testing is performed directly on the physical implementation of the network. The scenario where an adversary discovers a Security Misconfiguration in the Raspberry Pi 4 used as Sensor Server, i.e. unchanged default username and password. This is part of the OWASP Top 10:2021 [6], specifically A05 Security Misconfiguration, and holds the position for the fifth most common vulnerability, with an expected increase in occurrence with the industry moving towards highly configurable software.

The default username and password of the Raspberry pi account on Raspbian OS is pi and default respectively. It must be noted that Raspbian OS is notoriously insecure in the fact that it does not prompt for the root user password when commands on the terminal are preceded by the sudo keyword, thus it can be assumed that when an adversary gains remote access to the Raspberry pi server, they assume root privileges, thus compromising the system completely. 

The adversary gains access to the system while the program is running and can view all the other processes running. They can then end the python process which is the original program for the Sensor Server can be ended, and the adversary can attempt to connect with the Main Server.

![Adversary Viewing processes](https://user-images.githubusercontent.com/66631868/209849585-c336c9b0-043c-441c-9627-6d65dce9ea84.png)

_Figure 37: Adversary viewing all processes_

In the initial attempt, the adversary fails to connect as the Main Server accepts connection requests only at specific intervals in time, post which it is dormant to all communication requests. It is designed to sequentially accept requests from the Sensor server first, then the Actuator server, communicating with each of them in a fixed fashion prior to terminating connections. Thus, unless the adversary follows the exact same format for communication, the entire system fails, and the owners are alerted to the failure of the system, prompting an inspection.

![Adversary killing process](https://user-images.githubusercontent.com/66631868/209849578-bc692351-04db-409e-9641-f816e37fea95.png)

_Figure 38: Adversary killing legitimate processes_

![Main server Ending process](https://user-images.githubusercontent.com/66631868/209849593-43d7fa21-6afc-4873-8c72-660417cec323.png)

_Figure 39: Main Server error_

In the event of the adversary matching the timing of the request perfectly, the Main Server expects the SHA-256 hash of a predefined password for authentication of the Sensor Server. Failure to provide the same will cause the system to fail as well, alerting the owners and causing an inspection.

![Main server closing connection](https://user-images.githubusercontent.com/66631868/209849591-b4a21874-1c79-4f90-84c9-4f909fb7bcb1.png)

_Figure 40: Main Server closing connection_

![Adversary Unable to connect](https://user-images.githubusercontent.com/66631868/209849581-7c2381aa-e518-4313-a86f-caae5afb8c4a.png)

_Figure 41: Adversary unable to connect_


As the Raspbian OS does not prompt for root passwords when executing commands, the adversary can then view the code running on the initial server, and can identify the password being used to bypass the authentication mechanism of the Main Server. This vulnerability is also part of the OWASP Top 10:2021 [6], under the section A02 Cryptographic Failures. This leakage of sensitive data is exploited by the adversary to view the working of the communication between the Main Server and Sensor Server. 

![Cryptographic Failure](https://user-images.githubusercontent.com/66631868/209849589-ce300b48-9046-4b63-9788-6ebd21bcd19a.png)

_Figure 42: Cryptographic Failure_

Despite the adversary gaining access to the Main Server, they are unable to request the data stored in Logs due to design of the system. The only communication to the Sensor Server enabled is the sharing of the RSA public key. This Security by Design is the original idea of Zero-Trust as proposed by Kindervag [3]. Following this principle, the Main Server is designed to communicate very briefly with the Sensor Server, share the Public Key for encryption, receive the current data from the servers and immediately cease connection, closing the socket. It cannot be requested to send any data as it does not even support the functionality, and connection by any other socket is impossible because of the firewall blocking all other ports. Thus, while the real-time data can be stolen, all historical data stored in logs are secured. 


### 5. CONCLUSION

This work has been an attempt to demonstrate the principles of Zero-Trust security in an IoT setting, which is insecure by nature. Thus, following the principle of Security by Design, we have illustrated how data can be safeguarded from attacks by a malicious intruder, who has managed to completely compromise one of the three main servers of the architecture. 

The usage of temperature sensor, and ultrasonic sensor must be viewed as a placeholder for more significant and critical data such as monitoring a patient in a medical scenario, or the atmospheric conditions of a room containing artefacts. In these scenarios, the security of the data is of paramount importance, both in such that they cannot be tampered with, nor stolen. Thus, implementation of similarly designed networks in those scenarios would improve the security of the insecure IoT devices.

### 5.1 FUTURE SCOPE:

This is a very primitive implementation, and by taking into account the recommendations of industry standard practices, the security can be improved drastically. The security testing done is also very limited in scope and following the standards of an Industrial Red-teaming operation, i.e. thorough examination of the network by taking offensive action against the security will demonstrate the existence of further security flaws. 

This system currently lacks an Intrusion Detection and Prevention System (IDPS), nor is it robust. Thus the inclusion of an IDPS will further improve security as the IDPS will notify the administrator in the event of a breach, while the secure architecture followed by Zero-Trust based network will localise the threat, thus preventing the spread of the adversaries’ influence beyond a point. The robustness of the system must be improved such that the entire system does not fail in the event of an adversary’s attack, rather utilises the IDPS to identify the same and report it to the administrators.

### 6. REFERENCES:

1. Buck, C. Olenberger, C. Schweizer, A. Völter, F. and Eymann, T. (2021) ‘Never trust, always verify: A multivocal literature review on current knowledge and research gaps of zero-trust’, Computers & Security 110 102436
2. Friedman, J. (2020) ‘Definitive Guide to Zero Trust Security’
3. Kindervag, J. (2010) ‘Build Security Into Your Network’s DNA: The Zero Trust Network Architecture’
4. Mahajan, M. P. Nikam, R. R. Patil, V. P. Dond, R. D. (2017) ‘Smart Refrigerator Using IOT’, International Journal of Latest Engineering Research and Applications (IJLERA), Volume – 02, Issue – 03,  PP – 86-91
5. Palmo, Y. Tanimoto, S. Sato, S. and Kanai, A. (2021) ‘A Consideration of Scalability for Software Defined Perimeter Based on the Zero-trust Model’, 10th International Congress on Advanced Applied Informatics (IIAI-AAI)
6. owasp.org/Top10/
