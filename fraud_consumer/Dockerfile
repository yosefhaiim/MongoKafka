# שלב 1: להשתמש בתמונה בסיסית של Python
FROM python:3.12-slim

# הגדרת שם תיקיית העבודה בקונטיינר
WORKDIR /app

# העתקת קבצי requirements.txt לתוך הקונטיינר
COPY ../fraud_consumer/requirements.txt .

# התקנת התלויות הדרושות
RUN pip install --no-cache-dir -r requirements.txt

# העתקת כל הקבצים הנדרשים לתוך הקונטיינר
COPY . .

# הפעלת הסקריפט של הצרכן
CMD ["python", "fraud_consumer.py"]
