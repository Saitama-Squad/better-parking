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


ORG = "ev8xy3"
DEVICE_TYPE = "Camera"
TOKEN = "vl5?LaWJn1foPV(jzo"
DEVICE_ID = "00000004"
server = ORG + ".messaging.internetofthings.ibmcloud.com"
pubTopic = "iot-2/evt/status/fmt/json"
authMethod = "use-token-auth"
token = TOKEN
clientId = "d:"+ORG+":"+DEVICE_TYPE+":"+DEVICE_ID
mqttc = mqtt.Client(client_id=clientId)
mqttc.on_publish = on_publish
mqttc.on_connect = on_connect
mqttc.username_pw_set(authMethod, token)
mqttc.connect(server, 1883, 60)
mqttc.loop_start()

loop_flag = 1
pub_flag = 1
while loop_flag == 1:
    print('Awaiting Connection')
    sleep(1)

while True:
    ranInd = random.randint(1, 8)
    print(ranInd)
    data = {
        'grant_type': 'client_credentials',
        'client_id': os.environ.get('ZARA_4_API_CLIENT_ID'),
        'client_secret': os.environ.get('ZARA_4_API_CLIENT_SECRET'),
        'scope': 'image-processing,usage'
    }
    response = requests.post(
        'https://api.zara4.com/oauth/access_token', data=data).json()
    AT = response['access_token']
    files = {
        'access_token': (None, response['access_token']),
        'file': ('device/Images/'+str(ranInd)+'.jpeg', open('device/Images/'+str(ranInd)+'.jpg', 'rb')),
    }
    response = requests.post(
        'https://api.zara4.com/v1/image-processing/request', files=files).json()
    print(response)
    b64 = base64.b64encode(requests.get(
        response["generated-images"]["urls"][0]+'?access_token='+AT).content).decode('utf-8')
    metadata = {'id': DEVICE_ID, 'image': b64}
    payload = json.dumps(metadata)
    print(len(payload))
    mqttc.publish(pubTopic, payload=payload)
    pub_flag = 1
    while pub_flag == 1:
        print('Awaiting Publish Callback')
        sleep(1)
    for i in range(5, -1-1):
        print('Resending data in:', i)
        sleep(1)

mqttc.disconnect()
mqttc.loop_stop()
