#!/bin/bash

# Update package list and install dependencies
echo "Updating package list..."
sudo apt-get update

# Install Python and pip
echo "Installing Python and pip..."
sudo apt-get install -y python3 python3-pip

# Install necessary Python packages
echo "Installing Python packages..."
pip3 install kafka-python azure-storage-blob azure-mgmt-datalake-store pyarrow

# Install Scala if necessary (for Databricks)
if ! type "scala" > /dev/null; then
    echo "Installing Scala..."
    sudo apt-get install -y scala
fi

# Install and configure Kafka (assuming Debian-based system)
echo "Installing Kafka..."
wget https://downloads.apache.org/kafka/2.8.2/kafka_2.13-2.8.2.tgz
tar -xzf kafka_2.13-2.8.2.tgz
sudo mv kafka_2.13-2.8.2 /usr/local/kafka
echo "Kafka installed at /usr/local/kafka"

# Add Kafka to PATH
export PATH=$PATH:/usr/local/kafka/bin

echo "Setup completed."
