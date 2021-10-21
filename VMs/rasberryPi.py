import paho.mqtt.client as mqtt
import datetime
import random
import base64
import json
from time import sleep


def on_publish(client, payload, result):
    global pub_flag
    print("Data Published", datetime.datetime.now())
    pub_flag = 0


def on_connect(client, userdata, flags, rc):
    global loop_flag
    print(flags, rc)
    loop_flag = 0


ORG = "k8pfj3"
DEVICE_TYPE = "Camera"
TOKEN = "nihX-O0@y)hqnoZMx2"
DEVICE_ID = "080027391323"
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
    ranInd = random.randint(1, 3)
    print(ranInd)
    # with open(str(ranInd)+".jpeg", "rb") as img_file:
    #     b64 = base64.b64encode(img_file.read()).decode('utf-8')
    metadata = "hello"  # {'id':DEVICE_ID, 'image':b64}
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
