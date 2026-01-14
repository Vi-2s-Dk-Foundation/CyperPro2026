import requests

def check_ip_reputation(ip):
    # NOTE: This is a simulated URL for demonstration.
    url = f"[https://api.threatintel.com/check/](https://api.threatintel.com/check/){ip}"
    # Simulate a JSON response with a threat score
    if ip == "8.8.8.8":
        return {"ip": ip, "threat_score": 0, "status": "Clean"}
    else:
        return {"ip": ip, "threat_score": 95, "status": "Malicious"}
    
threat_status = check_ip_reputation("1.1.1.1")
print(f"IP {threat_status['ip']} Status: {threat_status['status']}")