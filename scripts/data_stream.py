from kafka import KafkaProducer
import json
import time
import random

# Kafka configuration
bootstrap_servers = 'localhost:9092'  # Change this if using a different Kafka setup
topic = 'optidata'

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize JSON data
)

def generate_data():
    # Generate sample data
    return {
        "timestamp": int(time.time()),  # Current timestamp
        "value": random.randint(1, 100)  # Random integer value
    }

def main():
    while True:
        data = generate_data()  # Generate data
        producer.send(topic, data)  # Send data to Kafka topic
        print(f"Sent: {data}")  # Print sent data for logging
        time.sleep(5)  # Wait for 5 seconds before sending next data

if __name__ == "__main__":
    main()
