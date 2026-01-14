# ==============================================================================
# Python Data Structures Demo for Cybersecurity
# Demonstrates Lists, Tuples, and Dictionaries using security-relevant examples.
# ==============================================================================

# 1. LISTS: Ordered, Mutable (Changeable). Used for dynamic collections.
# Use Case: Storing a list of suspicious IP addresses that needs to be updated 
# (added to or removed from) during an active incident.

print("--- 1. LISTS (Mutable Collection) ---")
suspicious_ips = [
    "192.168.1.10",
    "203.0.113.5",
    "172.16.0.25",
    "10.0.0.99"
]

print(f"Initial Suspicious IPs: {suspicious_ips}")
print(f"Number of IPs to block: {len(suspicious_ips)}")

# Add a new IP found during scanning (MUTABILITY)
suspicious_ips.append("1.2.3.4")
print(f"After Incident Update: {suspicious_ips}\n")


# 2. TUPLES: Ordered, Immutable (Unchangeable). Used for fixed records.
# Use Case: Defining static, known-good configurations or standard ports that 
# should never be altered during script execution.

print("--- 2. TUPLES (Immutable Record) ---")
# (Port Number, Protocol, Service Name) - This record should not change.
known_good_port = (22, "TCP", "SSH_SecureShell")

print(f"Known Good Record: {known_good_port}")
print(f"Service Name: {known_good_port[2]}")

# Attempting to change a tuple element will cause an error (IMMUTABILITY)
# known_good_port[0] = 8080 
# Uncommenting the line above would raise a TypeError.

print("Tuple is immutable, ensuring configuration integrity.\n")


# 3. DICTIONARIES: Unordered, Mutable. Used for key-value mapping (structured data).
# Use Case: Representing a single log entry or a JSON response from a Threat 
# Intelligence (TI) API, where fields are clearly defined.

print("--- 3. DICTIONARIES (Key-Value Mapping) ---")
threat_intel_report = {
    "ip_address": "45.77.12.55",
    "threat_score": 98,
    "category": "Malware C2",
    "last_seen": "2025-10-20"
}

print(f"Threat Score for {threat_intel_report['ip_address']}: {threat_intel_report['threat_score']}")

# Update the dictionary with new information (MUTABILITY)
threat_intel_report["status"] = "ACTIVE_BLOCK"
print(f"Updated status: {threat_intel_report['status']}")

print("\n--- Summary ---")
print("Lists: Dynamic IPs (mutable, order matters)")
print("Tuples: Fixed Configs (immutable, integrity)")
print("Dictionaries: Structured Logs (key-value, readable)")