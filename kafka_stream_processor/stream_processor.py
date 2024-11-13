from kafka import KafkaConsumer, KafkaProducer
import json
import time
import random
from datetime import datetime
import os

# הגדרת חיבור ל-Kafka
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')

# הגדרת Consumer ו-Producer
consumer = KafkaConsumer(
    'transactions',  # הנושא ממנו יצרוך העסקאות
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# קריטריונים לזיהוי הונאה
def is_fraudulent(transaction):
    if transaction['amount'] > 5000 or transaction['amount'] < 0.1 or transaction['is_fraudulent']:
        return True
    return False

# עיבוד עסקאות
def process_transactions():
    for message in consumer:
        transaction = message.value
        print(f"Received transaction: {transaction}")

        # בדיקת קריטריונים להונאה
        if is_fraudulent(transaction):
            # אם העסקה היא הונאה, נשלח לנושא fraud_transactions
            producer.send('fraud_transactions', value=transaction)
            print(f"Fraudulent transaction sent: {transaction}")
        elif transaction['amount'] > 3000:
            # אם העסקה היא בעלת ערך גבוה (מעל 3000), נשלח לנושא high_value_transactions
            producer.send('high_value_transactions', value=transaction)
            print(f"High value transaction sent: {transaction}")
        else:
            # אחרת, נשלח לנושא רגיל
            producer.send('regular_transactions', value=transaction)
            print(f"Regular transaction sent: {transaction}")

# הפעלת העיבוד
if __name__ == "__main__":
    process_transactions()
