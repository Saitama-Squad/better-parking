from json import load
from kafka import KafkaConsumer
import os
from dotenv import load_dotenv
load_dotenv()
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
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key,
                                         message.value))
