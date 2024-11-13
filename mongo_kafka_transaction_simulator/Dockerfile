# שלב 1: בחירת תמונת בסיס
FROM python:3.12-slim

# שלב 2: הגדרת משתנה הסביבה לעבודה
WORKDIR /app

# שלב 3: התקנת התלויות הדרושות
COPY requirements.txt simulator.py
RUN pip install --no-cache-dir -r requirements.txt

# שלב 4: העתקת קבצי הפרויקט לתוך התיקייה
COPY simulator.py .

# שלב 5: הפעלת הסקריפט
CMD ["python", "simulator.py"]
