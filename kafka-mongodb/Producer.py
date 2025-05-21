from time import sleep
from json import dumps
from kafka import KafkaProducer

topic_name = 'numtest'
kafka_server = 'localhost:9092'

producer = KafkaProducer(
    bootstrap_servers=kafka_server,
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

for e in range(1000):
    data = {'number': e}
    producer.send(topic_name, value=data)
    producer.flush()
    print(f"Sent: {data}")
    sleep(1)