---

# MongoKafka - Real-Time Fraud Detection System

## Overview

MongoKafka is a real-time fraud detection system that processes transaction data streams using Apache Kafka and stores the results in MongoDB. The system simulates transactions, processes them to detect fraudulent activities, and stores both high-value transactions and fraudulent transactions in MongoDB. Regular transactions are logged in CSV files for further analysis. The entire system is containerized using Docker and managed with Docker Compose for easy deployment.

---

## Features

- **Real-time Fraud Detection**: Uses Kafka to stream transaction data and process it in real-time to identify fraudulent activities.
- **Kafka Integration**: Leverages Kafka for high-throughput event streaming and message processing.
- **MongoDB Integration**: Fraudulent and high-value transactions are stored in MongoDB for later analysis.
- **CSV Logging**: Regular transactions are logged into CSV files.
- **Dockerized Environment**: The entire system is containerized with Docker and Docker Compose for easy setup and management.
- **Stream Processing**: Real-time processing of transactions for fraud detection using custom business logic.

---

## Project Structure

The project is organized as follows:

```
MongoKafka/
│
├── producer/
│   └── simulator.py                # Generates and sends random transaction data to Kafka.
│   └── Dockerfile                  # Dockerfile for the simulator service.
│
├── stream_processor/
│   └── stream_processor.py         # Processes incoming transactions and detects fraud.
│   └── Dockerfile                  # Dockerfile for the stream processor service.
│
├── fraud_consumer/
│   └── fraud_consumer.py           # Consumes fraudulent transactions and stores them in MongoDB.
│   └── Dockerfile                  # Dockerfile for the fraud consumer service.
│
├── high_value_consumer/
│   └── high_value_consumer.py      # Consumes high-value transactions and stores them in MongoDB.
│   └── Dockerfile                  # Dockerfile for the high-value consumer service.
│
├── transaction_logger/
│   └── transaction_logger.py       # Logs regular transactions into CSV files.
│   └── Dockerfile                  # Dockerfile for the transaction logger service.
│
├── mongo/
│   └── init.js                     # MongoDB initialization script (e.g., creating collections).
│
├── docker-compose.yml              # Docker Compose configuration for the entire system.
├── requirements.txt                # Python dependencies for the project.
└── README.md                       # Project documentation (this file).
```

---

## How to Run

To get the system up and running, follow these steps:

### 1. Build the Docker Containers

Make sure you have Docker and Docker Compose installed on your machine. Then, from the root of the project directory, run:

```bash
docker-compose build
```

This will build the necessary Docker images for all services in the project.

### 2. Start the Docker Containers

To start the services (Kafka, MongoDB, and all your custom services), run:

```bash
docker-compose up
```

This will start the following services:

- **Kafka**: Kafka broker for message streaming.
- **MongoDB**: MongoDB for storing fraudulent and high-value transactions.
- **Simulator**: A producer that generates random transaction data and sends it to Kafka.
- **Stream Processor**: Processes the transaction stream and identifies fraudulent transactions.
- **Fraud Consumer**: Consumes fraudulent transactions from Kafka and stores them in MongoDB.
- **High-Value Consumer**: Consumes high-value transactions from Kafka and stores them in MongoDB.
- **Transaction Logger**: Logs regular transactions into CSV files.

### 3. Verify the System

Once the system is running, you can verify the following:

- **Fraudulent Transactions**: Check MongoDB for the collection `fraudulent_transactions`.
- **High-Value Transactions**: Check MongoDB for the collection `high_value_transactions`.
- **Regular Transactions**: Look in the `transactions.csv` file for regular transactions.
  
You can also check the logs of each service using the following command:

```bash
docker-compose logs <service_name>
```

For example, to view logs for the fraud consumer, run:

```bash
docker-compose logs fraud_consumer
```

---

## Python Dependencies

The following dependencies are required for the project. These can be installed by running:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes:

```
kafka-python==2.0.0
pymongo==3.12.0
pandas==1.3.3
```

---

## Docker Compose Services

- **Kafka**: Kafka is used for streaming transaction data and processing messages asynchronously.
- **MongoDB**: MongoDB stores fraudulent and high-value transactions for later analysis.
- **Simulator**: The producer that simulates random transaction data and sends it to Kafka.
- **Stream Processor**: Processes transaction data from Kafka to detect fraudulent activities based on predefined criteria.
- **Fraud Consumer**: Consumes fraudulent transactions from Kafka and stores them in MongoDB.
- **High-Value Consumer**: Consumes high-value transactions and stores them in MongoDB.
- **Transaction Logger**: Logs regular transactions into CSV files.

---

## Troubleshooting

### Issue: Kafka Service Not Starting

Ensure that Kafka is properly configured and check the logs for any errors. You can view the Kafka logs using:

```bash
docker-compose logs kafka
```

### Issue: MongoDB Connection Failures

If the MongoDB service is not starting, check the MongoDB logs:

```bash
docker-compose logs mongo
```

Also, verify that MongoDB is reachable from your other containers by using the MongoDB URI `mongodb://mongo:27017` in your Python code.

---

## Conclusion

MongoKafka provides a complete solution for real-time fraud detection using Kafka for event streaming and MongoDB for storage. With Docker and Docker Compose, the entire system can be easily managed and scaled. This project serves as an excellent example of how to use stream processing, real-time data handling, and containerization for building production-ready systems.

---

**Feel free to modify or extend this project as needed!** If you have any questions or issues, open an issue or contact the maintainer.
![Fraud Detection System](images/README_image.png)

--- 
