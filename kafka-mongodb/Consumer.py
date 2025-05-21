from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads

topic_name = 'numtest'

consumer = KafkaConsumer(
    topic_name,
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

# MongoDB Atlas Connection
# Replace the below URI with your Atlas connection string
client = MongoClient("mongodb+srv://lmt:MatKhau123@cluster0.jedo2sp.mongodb.net/?retryWrites=true&w=majority")

collection = client['numtest']['numtest']  # database: numtest, collection: numtest
print("done")

for message in consumer:
    data = message.value
    collection.insert_one(data)
    print(f"{data} added to MongoDB Atlas")