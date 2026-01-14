import re
import random
from faker import Faker
from datetime import datetime, timedelta

def generate_fake_log_content(num_lines=500):
    """Generates a large string simulating Apache access log content."""
    fake = Faker()
    
    # Common resources and paths
    common_paths = [
        "/index.html", "/about/team.php", "/api/v1/data", "/assets/app.js",
        "/images/logo.png", "/css/main.css", "/robots.txt", "/sitemap.xml",
        "/blog/post/123", "/search?q=test"
    ]
    # Paths likely to cause 404s (e.g., old resources, common scans)
    not_found_paths = [
        "/nonexistent.php", "/admin/pma", "/old-page.html", "/login/forgot", 
        "/backup.zip", "/test.env", "/.git/config", "/wp-admin"
    ]
    
    # Status codes: bias towards 200 (normal traffic) but include common errors
    status_codes = [200] * 7 + [404] * 3 + [403] * 1 + [500] * 1
    
    # Methods
    methods = ['GET'] * 8 + ['POST'] * 2 + ['HEAD'] * 1

    log_lines = []
    current_time = datetime(2025, 1, 1, 10, 0, 0)
    
    for _ in range(num_lines):
        ip_address = fake.ipv4()
        method = random.choice(methods)
        
        # Decide the status code and path
        status = random.choice(status_codes)
        if status == 404:
            path = random.choice(not_found_paths)
        else:
            path = random.choice(common_paths)
            
        # Format the timestamp: [DD/Mon/YYYY:HH:MM:SS +0000]
        timestamp = current_time.strftime("[%d/%b/%Y:%H:%M:%S +0000]")
        
        # Request string
        request = f'"{method} {path} HTTP/1.1"'
        
        # Size of the response body
        size = random.randint(100, 5000)
        
        # Assemble the log line
        line = f'{ip_address} - - {timestamp} {request} {status} {size}'
        log_lines.append(line)
        
        # Increment time slightly for the next log entry
        current_time += timedelta(seconds=random.randint(1, 60))
        
    return "\n".join(log_lines)

# --- Generate Log Content ---
# Generate 500 lines of fake log data
log_content = generate_fake_log_content(num_lines=500)

# --- Analysis Setup ---
# Regex to capture IP and status code (specifically targeting 404)
# (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) : Group 1 (IP address)
# .*?"(?:GET|POST|PUT|DELETE)\s+.*?HTTP/\d\.\d" : Matches the middle part (request)
# \s+(404)\s+ : Group 2 (specifically captures 404 status code)
log_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?"(?:GET|POST|PUT|DELETE)\s+.*?HTTP/\d\.\d"\s+(404)\s+')

not_found_ips = set() # Using a set to store unique IPs

# --- Analysis Execution ---
for line in log_content.splitlines():
    match = log_pattern.search(line)
    if match:
        ip_address = match.group(1) # Group 1 is the IP
        status_code = match.group(2) # Group 2 is the status code (already known to be 404)
        not_found_ips.add(ip_address)

# --- Results ---
print("--- Analysis Report: Log File Simulation (500 lines) ---")
print(f"Total Unique IPs with 404 Not Found Errors found: {len(not_found_ips)}\n")

print("--- Unique IPs flagged for Excessive 404s (Potential Scanning/Misconfiguration) ---")
# Sort the set for consistent output
for ip in sorted(list(not_found_ips)): 
    print(f"| {ip}")