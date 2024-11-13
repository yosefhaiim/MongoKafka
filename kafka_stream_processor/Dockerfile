# השתמש בתמונה בסיסית של Python
FROM python:3.12-slim

# הגדרת תיקיית עבודה
WORKDIR /app

# העתקת קבצי requirements.txt ו- stream_processor.py
COPY requirements.txt /app/
COPY stream_processor.py /app/

# התקנת תלויות
RUN pip install --no-cache-dir -r requirements.txt

# הגדרת משתנים סביבתיים עבור Kafka
ENV KAFKA_BOOTSTRAP_SERVERS=localhost:9092

# הרצת הקוד
CMD ["python", "stream_processor.py"]
