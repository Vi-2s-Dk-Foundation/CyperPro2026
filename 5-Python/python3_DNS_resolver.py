import socket
hostname = "google.com"
try:
    ip = socket.gethostbyname(hostname)
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip}")
except socket.gaierror:
    print(f"Error: Could not resolve hostname {hostname}")
