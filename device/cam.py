import paho.mqtt.client as mqtt
import datetime
import random
import base64
import json
import os
from time import sleep
import requests
from dotenv import load_dotenv
load_dotenv()


def on_publish(client, payload, result):
    global pub_flag
    print("Data Published", datetime.datetime.now())
    pub_flag = 0


def on_connect(client, userdata, flags, rc):
    global loop_flag
    print(flags, rc)
    loop_flag = 0


def gen(DEVICE_ID):
    ORG = 'ev8xy3'
    DEVICE_TYPE = 'Camera'
    server = ORG + ".messaging.internetofthings.ibmcloud.com"
    clientId = "d:"+ORG+":"+DEVICE_TYPE+":"+DEVICE_ID
    return server, clientId


# MQTT Credentials
DEVICE_ID = "00000001"
pubTopic = "iot-2/evt/status/fmt/json"
authMethod = "use-token-auth"
token = '4!_eKg4kr3JYFhoX4L'
server, clientId = gen(DEVICE_ID)

# MQTT Connect
mqttc = mqtt.Client(client_id=clientId)
mqttc.on_publish = on_publish
mqttc.on_connect = on_connect
mqttc.username_pw_set(authMethod, token)
mqttc.connect(server, 1883, 60)
mqttc.loop_start()

loop_flag = 1
pub_flag = 1

while loop_flag == 1:
    # print('Awaiting Connection')
    # sleep(1)
    pass

# for i in range(1):
while True:
    # Simulating Capturing an Image
    ranInd = random.randint(1, 8)
    print(ranInd)
    # Zara4 Compression API (To compress captured image)

    # Request for temp access token
    # data = {
    #     'grant_type': 'client_credentials',
    #     'client_id': 'g4RH0pS7KzA7TCHN7Zd4urz7e7qrECRL6q2',
    #     'client_secret': 'uRISMAJ2jkTTZ8jeVJpGeLU2qym0WqYy2O1',
    #     'scope': 'image-processing,usage'
    # }
    # response = requests.post(
    #     'https://api.zara4.com/oauth/access_token', data=data).json()
    # AT = response['access_token']

    # #Request to compress file
    # files = {
    #     'access_token': (None, response['access_token']),
    #     'file': ('./Images/'+str(ranInd)+'.jpeg', open('./Images/'+str(ranInd)+'.jpg', 'rb')),
    # }
    # response = requests.post(
    #     'https://api.zara4.com/v1/image-processing/request', files=files).json()

    # Creating MQTT Payload
    img = open('device/Images/'+str(ranInd)+'.jpg', 'rb')
    img_data = img.read()
    b64 = base64.b64encode(img_data).decode('utf-8')
    metadata = {'id': random.randint(
        1, 30), 'floor': random.randint(1, 2), 'image': b64}
    payload = json.dumps(metadata)

    # Publish the Payload
    mqttc.publish(pubTopic, payload=payload)
    # pub_flag = 1
    sleep(1)
    while pub_flag == 1:
        # print('Awaiting Publish Callback')
        # sleep(1)
        pass

    # 5 second timer -> TODO : Change to AP Scheduler
    # (Connect -> Emit 2 Images -> Disconnect -> Wait 5 Seconds -> Repeat)
    for i in range(5, -1-1):
        print('Resending data in:', i)

    # TODO : Generate more keys for more devices
mqttc.disconnect()
mqttc.loop_stop()
