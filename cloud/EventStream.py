import wiotp.sdk.application
from wiotp.sdk.api.services import EventStreamsServiceBindingCredentials, EventStreamsServiceBindingCreateRequest
import json
import os
from kafka import KafkaProducer
from kafka.errors import KafkaError
from dotenv import load_dotenv
load_dotenv()

bootstrap_kafka_servers = 'broker-4-22l15k93cvmwf56x.kafka.svc07.us-south.eventstreams.cloud.ibm.com:9093,broker-3-22l15k93cvmwf56x.kafka.svc07.us-south.eventstreams.cloud.ibm.com:9093,broker-1-22l15k93cvmwf56x.kafka.svc07.us-south.eventstreams.cloud.ibm.com:9093,broker-0-22l15k93cvmwf56x.kafka.svc07.us-south.eventstreams.cloud.ibm.com:9093,broker-2-22l15k93cvmwf56x.kafka.svc07.us-south.eventstreams.cloud.ibm.com:9093,broker-5-22l15k93cvmwf56x.kafka.svc07.us-south.eventstreams.cloud.ibm.com:9093'.split(
    ',')
print("Starting Connection")
producer = KafkaProducer(bootstrap_servers=bootstrap_kafka_servers,
                         security_protocol='SASL_SSL', sasl_mechanism='PLAIN', sasl_plain_username='username', sasl_plain_password=os.environ.get('SASL_PLAIN_PASSWORD'), value_serializer=lambda m: json.dumps(m).encode('ascii'))
print("Kafka Broker Connected!")


def eventCallback(event):
    # str = "%s event '%s' received from device [%s]: %s"
    # print(str % (event.format, event.eventId,
    #       event.device, json.dumps(event.data)))
    data = json.dumps(event.data)
    producer.send('alldata',  {'data': data})
    print(f"Event {event.eventId} sent to kafka server!")


config = {
    "identity": {
        "appId": "app1"
    },
    "auth": {
        "key": "a-ev8xy3-rqfbn1jvy2",
        "token": "t_tSdBG-HVwcyOujtl"
    }
}

client = wiotp.sdk.application.ApplicationClient(config=config)
client.connect()
client.deviceEventCallback = eventCallback
client.subscribeToDeviceEvents(typeId="Camera")

while True:
    pass
