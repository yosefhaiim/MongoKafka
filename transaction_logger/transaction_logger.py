from kafka import KafkaConsumer
import json
import time
import logging
import os
from datetime import datetime
import pymongo

# הגדרת חיבור ל-Kafka
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')

# חיבור למונגוDB
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
client = pymongo.MongoClient(MONGO_URI)
db = client['fraud_detection']
transactions_collection = db['transactions_log']

# הגדרת Consumer של Kafka
consumer = KafkaConsumer(
    'transactions',  # נושא העסקאות
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# הגדרת לוגר
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# פונקציה לשמירת עסקאות למונגוDB
def log_transaction(transaction):
    try:
        transactions_collection.insert_one(transaction)
        logger.info(f"Transaction logged successfully: {transaction['transaction_id']}")
    except Exception as e:
        logger.error(f"Failed to log transaction {transaction['transaction_id']}: {e}")

# עיבוד וכתיבת עסקאות
def process_transactions():
    for message in consumer:
        transaction = message.value
        print(f"Received transaction: {transaction}")

        # שמירת העסקה למונגוDB
        log_transaction(transaction)

        # אפשרות להוסיף כאן גם לוגיקה נוספת כמו זיהוי הונאה או עיבוד נוסף

# הפעלת העיבוד
if __name__ == "__main__":
    process_transactions()
