import socket
target = "127.0.0.1" # Target localhost for safety
common_ports = [21, 22, 23, 80, 443]

for port in common_ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5) # Fast check
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} OPEN on {target}")
    sock.close()

print("Simple Port Scanning COMPLETED!")