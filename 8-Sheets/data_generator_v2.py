from faker import Faker
import csv
import random
from datetime import datetime, timedelta

fake = Faker()

START_DATE = datetime(2022, 1, 1)
END_DATE = datetime(2025, 12, 31)

def random_date():
    delta = END_DATE - START_DATE
    return START_DATE + timedelta(days=random.randint(0, delta.days))

def enrich_time_fields(dt):
    return {
        "date": dt.strftime("%Y-%m-%d"),
        "week": dt.strftime("%Y-W%U"),
        "month": dt.strftime("%Y-%m"),
        "year": dt.year
    }

# ---------------- FIREWALL LOGS ----------------
def generate_firewall_logs(num_entries):
    rows = []
    for _ in range(num_entries):
        ts = random_date()
        t = enrich_time_fields(ts)

        rows.append([
            ts.strftime("%Y-%m-%d %H:%M:%S"),
            t["date"], t["week"], t["month"], t["year"],
            fake.ipv4_public(),
            fake.ipv4_public(),
            random.randint(1, 65535),
            random.choice(["TCP", "UDP"]),
            random.choice(["Allowed", "Blocked"])
        ])
    return rows

# ---------------- VULNERABILITY SCAN ----------------
def generate_vulnerabilities(num_entries):
    rows = []
    os_list = ["Windows 10", "Windows 11", "Windows Server 2022", "Ubuntu 22.04"]

    for _ in range(num_entries):
        ts = random_date()
        t = enrich_time_fields(ts)

        cve = f"CVE-{random.randint(2021, 2025)}-{random.randint(1000, 9999)}"

        rows.append([
            ts.strftime("%Y-%m-%d"),
            t["week"], t["month"], t["year"],
            fake.hostname(),
            fake.ipv4_public(),
            cve,
            random.randint(1, 10),
            random.choice(os_list)
        ])
    return rows

# ---------------- THREAT INTELLIGENCE ----------------
def generate_threat_intel(num_entries):
    rows = []
    threat_types = ["RCE", "Botnet", "APT Activity", "Exploited CVE", "Zero-Day"]

    for _ in range(num_entries):
        ts = random_date()
        t = enrich_time_fields(ts)

        ioc_type = random.choice(["CVE", "IP", "Domain"])
        if ioc_type == "CVE":
            ioc = f"CVE-{random.randint(2021, 2025)}-{random.randint(1000, 9999)}"
        elif ioc_type == "IP":
            ioc = fake.ipv4_public()
        else:
            ioc = fake.domain_name()

        rows.append([
            ts.strftime("%Y-%m-%d"),
            t["week"], t["month"], t["year"],
            ioc,
            random.choice(threat_types),
            random.choice(["Low", "Medium", "High", "Critical"])
        ])
    return rows

# ---------------- WRITE CSVs ----------------
with open("firewall_logs.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "Timestamp", "Date", "Week", "Month", "Year",
        "Source IP", "Destination IP", "Port", "Protocol", "Action"
    ])
    writer.writerows(generate_firewall_logs(3000))

with open("vulnerability_scan.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "Date", "Week", "Month", "Year",
        "Hostname", "IP Address", "CVE", "Severity", "OS"
    ])
    writer.writerows(generate_vulnerabilities(2000))

with open("threat_intelligence.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "Date", "Week", "Month", "Year",
        "IOC", "Threat Type", "Risk Level"
    ])
    writer.writerows(generate_threat_intel(1500))

print("✅ Module 8 datasets generated successfully")
