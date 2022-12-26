# SImple-Zero-Trust

### ABSTRACT:

The Internet of Things (IoT) is one of the novel concepts which has taken the world by storm. The ability to integrate regular home appliances on the internet allowing remote access from anywhere has been progressing rapidly. Although the technology holds many advantages, the security concerns in these systems make them double-edged swords. Zero-Trust has been introduced in the security industry as the answer to most cyber threats present. The segmentation of access rights, even within internal nodes of the system is a key feature of this model.
Our project titled “Trust-Free Homes: An Analysis of Performance and Scalability of the Zero-Trust paradigm in Smart Home systems”, aims at implementing a Zero - Trust System to analyse its capabilities in IoT networks. The limited capabilities of IoT devices makes running multiple key-generation algorithms, and key-storage a point of concern, and implementing Zero-Trust without affecting their regular functioning at scale is a challenge. The project will be carried out by simulating the behaviour of IoT devices using Azure’s simulation capabilities for modelling the network, then using Python for implementing a working system on a very small IoT network.
The efficiency of the implemented Zero-Trust network will be scrutinised, and possible improvements to implementations will be tried. This project is aimed at serving as a guide to a working model of the Zero-Trust guidelines.

### 1. INTRODUCTION:
Internet-of-Things (IoT) is one the key concepts leading into Industry 4.0. It is the integration of all devices over a single network, effectively communicating to one another, setting up a continuous stream of data allowing all devices on the network to access the same for effective decision-making, thus improving the state-of-art of industries. All this data is freely accessible and is stored on low-power, limited capability IoT devices, thus severely crippling the security for the same. The state of the cyber-landscape is such that the more integrated and exposed a system is, the easier it is for malicious actors to exploit the same. IoT is particularly at risk, due to low grade of security in IoT devices. 

Among the many methods proposed and used in the industry to secure the same, the Zero-Trust Paradigm is a promising new idea. Its novelty lies in the fact that unlike traditional perimeter-based methods, Zero-Trust preaches complete isolation and segmentation, even within a network. It aims to secure all data and functionality of the network and its nodes by verifying and encrypting all data and communications, as well as granting only required privileges post authentication on-demand.

Zero-Trust functions on the motto, “Never Trust, Always Verify”. This policy of segmentation and verification safeguards sensitive data from the threat of compromised internal nodes. The segmentation localises the compromise to a specific area, following which the Intrusion Detection and Prevention System (IDPS) notifies the administrator about the security breach and takes further preventive measures to stop the leakage of data.

Zero-Trust has an edge over perimeter based security because of the human factor in security breaches. Weak passwords, unchanged router or server default passwords, accidental introduction of malware into internal nodes are all possible with human intervention. Unfortunately, human intervention is also required for smooth functioning of many networks, as well as the repair and recovery of many compromised networks. Thus, setting external perimeters alone compromises the overall security of the network, due to high risk of compromise of an internal node, within the perimeter.

Despite the obvious advantages in adopting Zero-Trust, it still is an idea, and there is no codification in guidelines of adoption. There are multiple implementations by multiple organisations, each tailoring the guidelines to match their requirements. The lack of standardisation, combined with the need for investment in changing the landscape of the internal network have been major detriments to the adoption of this paradigm.

### 1.1. OBJECTIVES:
This work has the following objectives:
- Simulate an IoT network by building everything from the basic connections and implementing a basic security model in accordance to the Zero-Trust principles.
- Verify the adaptability of the security model by deploying it in a similar IoT network.
- Demonstrate security of the implemented security model.

The report is structured as follows: the literature considered and their key points are first described, post which there is a detailed explanation of Zero-Trust model, followed by the methodology adopted by the project. Prior to the design of the Zero-Trust model, an IoT network is simulated and the architecture and working is explained. This is followed by the description of the implemented Zero-Trust model, and the explanation of what principles each change satisfies. This is followed by the description of the physical IoT network built to match the architecture of the simulated IoT network, and illustrates the deployment of the Zero-Trust model in the same. This is finally followed by an illustration of capabilities of a malicious agent, who is assumed to have compromised and escalated privileges in one of the IoT devices.

### LITERATURE SURVEY:

In the article by Buck et al [1], the authors provide an overview on the current trends and research interests in the field of Zero-Trust security. Equal importance is given to grey literature as well, apart from academic literature due to the pioneering work in implementations done by the industry.

Kindervag [3] in his pioneering work on Zero-Trust illustrates the prime focus of a Zero-Trust network architecture. The work differentiates the traditional architecture where security is an overlay from the Zero-Trust architecture envisioned in 2010, where security is an integral component of the very core of the architecture. 

Friedman’s [2] work provides detailed insight into the Zero-Trust paradigm. It cohesively explains the failure of the promise of traditional security, followed by the promise of Zero-Trust. It further elaborates on the security landscape, describes methods to define and protect different zones on the landscape, each of a different level of required security.
 
In the IEEE paper by Palmo et al [5], the authors provide insight into a Software-Defined Perimeters (SDP), a security model built with Zero-Trust in mind. They outlined the disadvantages of existing SDN models and proposed scalable SDN architectures which satisfy modern network requirements.

The article by Mahajan et al. [4] provides insight into basics of IoT, and the necessary description of the simple IoT network envisioned for this project. It describes the components required and working for an IoT based Smart Refrigerator, and the methodology used for the working of the same. We have taken inspiration from the same to build the physical IoT network on which the constructed Zero-Trust model is deployed.

### THE ZERO-TRUST PARADIGM

All traditional security models are based on trust. Some networks are trusted, some users are trusted and some devices are trusted. This trust boundary is established by very stringent firewalls, rigorous whitelisting of data and constant monitoring of all incoming and outgoing data. This security model has been relatively successful, barring one special case of malicious actors, i.e. the malicious insider. This is the scenario where a user, device or network classified as “trusted” acts as the source of malicious activity. In this case, the basic premise of the security system fails, and the malicious agent wrecks havoc on the network. 

Improving security comes as a result of changing the model of trust. Zero-Trust model is a proposition that does the same. It applies the same conditions and regulations it does to a node from an internal system that it does to a node from an external system.  This means encryption, verification and authentication of all devices, as well as providing access to network resources and data on a need-only basis. Zero-Trust does not mean not to trust the employees of an organisation, rather it applies to the data and communications being transferred around in the network of the organisation.

One of the advantages of the Zero-Trust model is that it is platform agnostic. The same principles can be applied to all platforms and networks, achieving the expected result. It is also highly scalable, for the newer segments of the network can be integrated along with older segments effectively. It can effectively replace an existing system, as the architecture of the Zero-Trust system is inside-out, i.e. smaller segments are completely secured prior to integrating all segments together. Once the segments are integrated, the connections between segments are secured as well.
It must be noted that the smaller components of security, namely firewalls, VPNs, whitelists, access control mechanisms, intrusion prevention systems, cryptography, etc. are not obsolete in this model, rather their method of deployment is altered. They are used extensively in the boundaries between segments, for encrypting all communications of the network, and to provide access to resources on the need-only basis. Apart from all this, all data is logged and stored for future reference.

![Sample Zero - Trust Process Flowchart]((https://github.com/AdityaDamodhar25/SImple-Zero-Trust/blob/main/Project%20Description/Report%20Images/Sample%20Zero%20Trust%20Process%20Flowchart.png))
_Figure 1: Zero - Trust Process Flowchart_

