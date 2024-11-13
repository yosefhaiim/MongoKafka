from kafka import KafkaConsumer
import json
import pymongo
import os

# הגדרת החיבור ל-Kafka ול-MongoDB
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017')

# הגדרת Consumer של Kafka
consumer = KafkaConsumer(
    'transactions',  # שמו של הנושא (topic) ב-Kafka
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    group_id='fraud-consumer-group',  # שם קבוצת הצרכנים
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # המרה ממידע גולמי לאובייקט JSON
)

# חיבור ל-MongoDB
client = pymongo.MongoClient(MONGO_URI)
db = client['transactions_db']  # שם בסיס הנתונים ב-MongoDB
fraud_collection = db['fraud_transactions']  # שם האוסף בו יישמרו עסקאות ההונאה

# לולאת צרכן: מקבלת הודעות מ-Kafka ומאחסנת את העסקאות המזהות כ'הונאה' ב-MongoDB
for message in consumer:
    transaction = message.value  # קבלת הנתונים מההודעה
    if transaction['is_fraudulent']:  # אם העסקה היא הונאה
        print(f"Detected fraudulent transaction: {transaction}")
        fraud_collection.insert_one(transaction)  # שמירת העסקה בהונאה ב-MongoDB

