from faker import Faker
import random, csv
from datetime import datetime, timedelta

fake = Faker()
start_date = datetime(2024, 1, 1)

events = ["Login Failure", "Malware Detected", "Port Scan", "Policy Violation"]
severities = ["Low", "Medium", "High", "Critical"]
assets = ["Web-Server", "DB-Server", "Endpoint", "Firewall"]
sources = ["SIEM", "EDR", "Firewall", "IDS"]

with open("security_events_year.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "Timestamp","Date","Week","Month",
        "Event_Type","Severity","Asset","Source"
    ])

    for i in range(12000):
        ts = start_date + timedelta(minutes=random.randint(0, 525600))
        writer.writerow([
            ts,
            ts.date(),
            ts.isocalendar()[1],
            ts.strftime("%Y-%m"),
            random.choice(events),
            random.choice(severities),
            random.choice(assets),
            random.choice(sources)
        ])
