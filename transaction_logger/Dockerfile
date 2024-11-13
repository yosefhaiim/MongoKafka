# השתמש בתמונה בסיסית של Python
FROM python:3.12-slim

# הגדרת תיקיית עבודה
WORKDIR /app

# העתקת קבצי requirements.txt ו- transaction_logger.py
COPY requirements.txt /app/
COPY transaction_logger.py /app/

# התקנת תלויות
RUN pip install --no-cache-dir -r requirements.txt

# הגדרת משתנים סביבתיים עבור Kafka ומונגוDB
ENV KAFKA_BOOTSTRAP_SERVERS=localhost:9092
ENV MONGO_URI=mongodb://localhost:27017

# הרצת הקוד
CMD ["python", "transaction_logger.py"]
