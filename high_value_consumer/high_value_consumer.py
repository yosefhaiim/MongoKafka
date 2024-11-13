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
    group_id='high-value-consumer-group',  # שם קבוצת הצרכנים
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # המרה ממידע גולמי לאובייקט JSON
)

# חיבור ל-MongoDB
client = pymongo.MongoClient(MONGO_URI)
db = client['transactions_db']  # שם בסיס הנתונים ב-MongoDB
high_value_collection = db['high_value_transactions']  # שם האוסף בו יישמרו עסקאות בעלות ערך גבוה

# לולאת צרכן: מקבלת הודעות מ-Kafka ומאחסנת רק את העסקאות בעלות ערך גבוה ב-MongoDB
for message in consumer:
    transaction = message.value  # קבלת הנתונים מההודעה
    if transaction['amount'] > 5000:  # אם העסקה בעלת ערך גבוה מ-5000
        print(f"Detected high-value transaction: {transaction}")
        high_value_collection.insert_one(transaction)  # שמירת העסקה בעלת הערך הגבוה ב-MongoDB
