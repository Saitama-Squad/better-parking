from json import load
from kafka import KafkaConsumer
import os
from dotenv import load_dotenv
from ast import literal_eval
import json
import numpy as np
import base64
from PIL import Image
import io
import matplotlib.pyplot as plt

load_dotenv()

def bytestojson(bytes):
    data = literal_eval(bytes.decode('utf8'))
    s = json.loads(json.dumps(data, indent=4, sort_keys=True))
    s["data"] = json.loads(s["data"])
    b64toimage(s["data"]["image"])

def b64toimage(b64):
    base64_decoded = base64.b64decode(b64)
    image = Image.open(io.BytesIO(base64_decoded))
    image_np = np.array(image)
    print(image_np)
    image.save('a.jpg')

bootstrap_kafka_servers = [
    os.environ.get('BROKER1'),
    os.environ.get('BROKER2'),
    os.environ.get('BROKER3'),
    os.environ.get('BROKER4'),
    os.environ.get('BROKER5'),
    os.environ.get('BROKER6')
]

print("Starting Connection")
consumer = KafkaConsumer('alldata',
                         bootstrap_servers=bootstrap_kafka_servers,
                         security_protocol='SASL_SSL',
                         sasl_mechanism='PLAIN',
                         sasl_plain_username='username',
                         sasl_plain_password=os.environ.get('SASL_PASSWORD')
                         )
print("Connected!")
print(consumer.bootstrap_connected)

# Asynchronous by default
for message in consumer:
    print("Printing Message")
    bytestojson(message.value)
