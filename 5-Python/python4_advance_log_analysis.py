# Simulate a log file (in a real scenario, you'd open an actual file)
log_content = """
192.168.1.1 - [01/Jan/2024:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.5 - [01/Jan/2024:10:05:15 +0000] "GET /nonexistent.php HTTP/1.1" 404 567
10.0.0.10 - [01/Jan/2024:10:10:30 +0000] "POST /login HTTP/1.1" 200 890
192.168.1.5 - [01/Jan/2024:10:15:45 +0000] "GET /another-missing.css HTTP/1.1" 404 123
172.16.0.20 - [01/Jan/2024:10:20:00 +0000] "GET /admin HTTP/1.1" 403 456
"""

# In a real script, you'd use:
# with open('access.log', 'r') as f:
#     log_content = f.read()

import re

# Regex to capture IP and status code
# \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} : IP address pattern
# \s+\S+ : space and non-space characters (username, etc.)
# \[.*?\] : timestamp in brackets
# ".*?" : quoted request
# \s+(\d{3}) : space followed by 3 digits (status code)
log_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?"(?:GET|POST|PUT|DELETE)\s+.*?HTTP/\d\.\d"\s+(404)\s+')

not_found_ips = set() # Using a set to store unique IPs

for line in log_content.splitlines():
    match = log_pattern.search(line)
    if match:
        ip_address = match.group(1) # Group 1 is the IP
        status_code = match.group(2) # Group 2 is the status code (which we know is 404)
        not_found_ips.add(ip_address)

print("\n--- Unique IPs with 404 Not Found Errors ---")
for ip in sorted(list(not_found_ips)): # Sort for consistent output
    print(ip)