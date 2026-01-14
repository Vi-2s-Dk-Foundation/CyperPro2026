from faker import Faker
import csv
import random
from datetime import datetime, timedelta

fake = Faker()

def generate_firewall_log(num_entries):
    data = []
    start_date = datetime(2024, 7, 26, 8, 0, 0)
    for _ in range(num_entries):
        timestamp = start_date + timedelta(minutes=random.randint(0, 1440))  # Up to 24 hours
        source_ip = fake.ipv4_public()  # Or fake.ipv4_private()
        dest_ip = fake.ipv4_public()
        port = random.randint(1, 65535)
        protocol = random.choice(["TCP", "UDP", "ICMP"])
        action = random.choice(["Allowed", "Blocked"])
        data.append([timestamp.strftime("%Y-%m-%d %H:%M:%S"), source_ip, dest_ip, port, protocol, action])
    return data

def generate_vulnerability_data(num_entries):
    data = []
    operating_systems = ["Windows 10", "Windows 11", "Windows Server 2019", "Windows Server 2022", "Linux"]
    for _ in range(num_entries):
        hostname = fake.hostname()
        ip_address = fake.ipv4_public()
        cve_id = f"CVE-{random.randint(2020, 2024)}-{random.randint(1000, 9999)}"
        severity = random.randint(1, 9)  # 1-9 scale
        os = random.choice(operating_systems)
        data.append([hostname, ip_address, cve_id, severity, os])
    return data

def generate_threat_intel(num_entries):
    data = []
    threat_types = ["Malicious IP", "Known Attacker", "Remote Code Execution", "Phishing Domain", "Malicious File Hash (SHA-256)", "Botnet C2"]
    for _ in range(num_entries):
        ioc_type = random.choice(["ip_address", "domain_name", "cve_id", "file_hash"])
        if ioc_type == "ip_address":
            ioc = fake.ipv4_public()
        elif ioc_type == "domain_name":
            ioc = fake.domain_name()
        elif ioc_type == "cve_id":
            ioc = f"CVE-{random.randint(2020, 2024)}-{random.randint(1000, 9999)}"
        elif ioc_type == "file_hash":
            ioc = fake.sha256()
        data.append([ioc, random.choice(threat_types)])
    return data


# Generate and save data to CSV files
firewall_data = generate_firewall_log(500)  # Generate 500 entries (adjust as needed)
with open("firewall_logs.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Timestamp", "Source IP", "Destination IP", "Port", "Protocol", "Action"])
    writer.writerows(firewall_data)

vulnerability_data = generate_vulnerability_data(300)  # Generate 300 entries
with open("vulnerability_scan.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Hostname", "IP Address", "Vulnerability ID", "Severity", "Operating System"])
    writer.writerows(vulnerability_data)


threat_intel_data = generate_threat_intel(200)  # Generate 200 entries
with open("threat_intelligence.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["IOC", "Threat Type"])
    writer.writerows(threat_intel_data)

print("Data generated and saved to CSV files.")