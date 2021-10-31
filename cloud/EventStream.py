import wiotp.sdk.application
import json
from kafka import KafkaProducer
import os
from dotenv import load_dotenv
load_dotenv()
def eventCallback(event):
    data = json.dumps(event.data)
    producer.send('alldata',  {'data': data})
    print(f"Event {event.eventId} sent to kafka server!")

bootstrap_kafka_servers = [
    os.environ.get('BROKER1'),
    os.environ.get('BROKER2'),
    os.environ.get('BROKER3'),
    os.environ.get('BROKER4'),
    os.environ.get('BROKER5'),
    os.environ.get('BROKER6')
]

config = {
    "identity": {
        "appId": "app1"
    },
    "auth": {
        "key": os.environ.get('WIOTP_KEY'),
        "token": os.environ.get('WIOTP_TOKEN') 
    }
}

print("Starting Connection")

producer = KafkaProducer(
    bootstrap_servers=bootstrap_kafka_servers,
    security_protocol='SASL_SSL',
    sasl_mechanism='PLAIN',
    sasl_plain_username='username',
    sasl_plain_password= os.environ.get('SASL_PASSWORD'),
    value_serializer=lambda m: json.dumps(m).encode('ascii')
)

print("Kafka Broker Connected!")

client = wiotp.sdk.application.ApplicationClient(config=config)
client.connect()
client.deviceEventCallback = eventCallback
client.subscribeToDeviceEvents(typeId="Camera")

while True:
    pass
