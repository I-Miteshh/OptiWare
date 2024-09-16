from kafka import KafkaConsumer
import json

# Kafka configuration
bootstrap_servers = 'localhost:9092'
topic = 'optidata'

# Initialize Kafka consumer
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=bootstrap_servers,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    print(f"Received: {message.value}")
