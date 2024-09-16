from kafka import KafkaProducer
import json
import time
import random

# Kafka configuration
bootstrap_servers = 'localhost:9092'
topic = 'optidata'

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_data():
    # Generate sample data
    return {
        "timestamp": int(time.time()),
        "value": random.randint(1, 100)
    }

while True:
    data = generate_data()
    producer.send(topic, data)
    print(f"Sent: {data}")
    time.sleep(5)  # Send data every 5 seconds
