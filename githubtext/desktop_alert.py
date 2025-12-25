from plyer import notification
from datetime import datetime
import time
import mysql.connector
import platform

db = mysql.connector.connect(host="localhost", user="root", password="rithi272", database="emp_db")
cursor = db.cursor(dictionary=True)

while True:
    now = datetime.now().strftime("%H:%M")
    cursor.execute("SELECT * FROM alerts WHERE shown=0 AND time=%s", (now,))
    alerts = cursor.fetchall()
    for alert in alerts:
        if platform.system() in ["Windows","Linux","Darwin"]:
            notification.notify(title="🔔 Alert", message=alert["message"], timeout=10)
        cursor.execute("UPDATE alerts SET shown=1 WHERE id=%s", (alert["id"],))
        db.commit()
    time.sleep(30)  