from kafka import KafkaProducer
from kafka.errors import KafkaError
import json

bootstrap_kafka_servers = 'broker-4-22l15k93cvmwf56x.kafka.svc07.us-south.eventstreams.cloud.ibm.com:9093,broker-3-22l15k93cvmwf56x.kafka.svc07.us-south.eventstreams.cloud.ibm.com:9093,broker-1-22l15k93cvmwf56x.kafka.svc07.us-south.eventstreams.cloud.ibm.com:9093,broker-0-22l15k93cvmwf56x.kafka.svc07.us-south.eventstreams.cloud.ibm.com:9093,broker-2-22l15k93cvmwf56x.kafka.svc07.us-south.eventstreams.cloud.ibm.com:9093,broker-5-22l15k93cvmwf56x.kafka.svc07.us-south.eventstreams.cloud.ibm.com:9093'.split(
    ',')
print("Starting Connection")
producer = KafkaProducer(bootstrap_servers=bootstrap_kafka_servers,
                         security_protocol='SASL_SSL', sasl_mechanism='PLAIN', sasl_plain_username='username', sasl_plain_password='6FSKZVw-tKGxYSOShuUlbE37QU5kZM9ELp4iI2Nc0C5I')
print("Connected!")
print(producer.bootstrap_connected)

# Asynchronous by default
future = producer.send('alldata', b'hello world from python')

# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    # Decide what to do if produce request failed...
    print("Exception")
    pass
print("Sent! 23")

# Successful result returns assigned partition and offset
print(record_metadata.topic)
print(record_metadata.partition)
print(record_metadata.offset)
# producer.close()

# # produce json messages
# producer = KafkaProducer(bootstrap_servers=bootstrap_kafka_servers,
#                          security_protocol='SASL_SSL', sasl_mechanism='PLAIN', sasl_plain_username='username', sasl_plain_password='6FSKZVw-tKGxYSOShuUlbE37QU5kZM9ELp4iI2Nc0C5I',
#                          value_serializer=lambda m: json.dumps(m).encode('ascii'))
# producer.send('alldata', {'key': 'value'})
# print("Sent! 36")

# produce asynchronously
for _ in range(10):
    producer.send('alldata', b'msg')
    print("Sent! 41")


def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)


def on_send_error(excp):
    print('I am an errback', excp)
    # handle exception


# produce asynchronously with callbacks
producer.send(
    'alldata', b'raw_bytes').add_callback(on_send_success).add_errback(on_send_error)

# block until all async messages are sent
producer.flush()
