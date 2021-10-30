from kafka import KafkaConsumer
from kafka.errors import KafkaError
import json

bootstrap_kafka_servers = 'broker-4-22l15k93cvmwf56x.kafka.svc07.us-south.eventstreams.cloud.ibm.com:9093,broker-3-22l15k93cvmwf56x.kafka.svc07.us-south.eventstreams.cloud.ibm.com:9093,broker-1-22l15k93cvmwf56x.kafka.svc07.us-south.eventstreams.cloud.ibm.com:9093,broker-0-22l15k93cvmwf56x.kafka.svc07.us-south.eventstreams.cloud.ibm.com:9093,broker-2-22l15k93cvmwf56x.kafka.svc07.us-south.eventstreams.cloud.ibm.com:9093,broker-5-22l15k93cvmwf56x.kafka.svc07.us-south.eventstreams.cloud.ibm.com:9093'.split(
    ',')
print("Starting Connection")
consumer = KafkaConsumer('alldata',
                         bootstrap_servers=bootstrap_kafka_servers, security_protocol='SASL_SSL', sasl_mechanism='PLAIN', sasl_plain_username='username', sasl_plain_password='6FSKZVw-tKGxYSOShuUlbE37QU5kZM9ELp4iI2Nc0C5I')
print("Connected!")
print(consumer.bootstrap_connected)

# Asynchronous by default
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print("Printing Message")
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key,
                                         message.value))
