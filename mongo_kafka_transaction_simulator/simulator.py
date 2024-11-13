
from kafka import KafkaProducer
import json
import random
import time
from datetime import datetime

# רשימת משתמשים ורשימת משתמשים חסומים
user_ids = [f"user_{i}" for i in range(1, 10001)]
blacklisted_users = random.sample(user_ids, 10)  # בוחרים 10 משתמשים לרשימה השחורה

# Producer של Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# יצירת עסקה אקראית
def create_transaction():
    user_id = random.choice(user_ids)
    amount = round(random.uniform(0.01, 7500), 2)
    is_fraudulent = amount > 5000 or amount < 0.1 or user_id in blacklisted_users
    transaction = {
        "transaction_id": f"txn_{random.randint(100000, 999999)}",
        "user_id": user_id,
        "amount": amount,
        "timestamp": datetime.utcnow().isoformat(),
        "is_fraudulent": is_fraudulent
    }
    return transaction

# שליחת הודעות ל-Kafka
while True:
    transaction = create_transaction()
    producer.send('transactions', value=transaction)
    print(f"Sent transaction: {transaction}")
    time.sleep(random.uniform(0.1, 1))  # המתנה אקראית בין הודעות