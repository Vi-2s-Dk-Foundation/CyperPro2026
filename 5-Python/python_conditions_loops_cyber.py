# ==============================================================================
# Python Control Flow Demo for Cybersecurity
# Demonstrates Conditionals (if/elif/else) and Loops (for/while)
# using security-relevant examples.
# ==============================================================================

# --- 1. CONDITIONAL STATEMENTS (if/elif/else) ---
# Use Case: Simple Intrusion Detection System (IDS) Logic
# Task: Analyze a log entry (a dictionary) and determine the severity of the event.

print("--- 1. CONDITIONAL STATEMENTS (Intrusion Detection) ---")

event_log_entry = {
    "source_ip": "10.10.1.5",
    "event_type": "FAILED_LOGIN",
    "attempts": 5
}

# The threshold for a high-severity event
HIGH_SEVERITY_THRESHOLD = 3

print(f"Analyzing event from {event_log_entry['source_ip']}...")
print(f"Event Type: {event_log_entry['event_type']}, Attempts: {event_log_entry['attempts']}")

if event_log_entry["event_type"] == "SQL_INJECTION":
    # Highest priority
    print("ALERT: CRITICAL - SQL Injection attempt detected. Immediate lockdown required.")
elif event_log_entry["event_type"] == "FAILED_LOGIN" and event_log_entry["attempts"] >= HIGH_SEVERITY_THRESHOLD:
    # High priority due to repeated failure (potential brute force)
    print("WARNING: HIGH - Excessive failed login attempts. Block IP and investigate.")
elif event_log_entry["event_type"] == "SCANNING_ACTIVITY":
    # Low priority, usually passive monitoring
    print("NOTICE: LOW - Routine port scanning activity detected. Monitor only.")
else:
    # Default case
    print("INFO: Event within normal operating parameters. Logged.")

print("-" * 40)

# --- 2. FOR LOOP ---
# Use Case: Password Hash Cracking (Iterating through a list of possible passwords)
# Task: Test a list of common passwords against a known, weak hash.

print("--- 2. FOR LOOP (Password Cracking Simulation) ---")

common_passwords = ["password123", "admin", "qwert", "shadow", "P@sswOrd"]
target_hash = "shadow"  # In a real scenario, this would be a complex hash like SHA-256

print(f"Target Hash (Weak Hash Simulation): '{target_hash}'")

for password in common_passwords:
    print(f"Testing password: {password}")
    
    # Conditional logic inside the loop
    if password == target_hash:
        print(f"\nSUCCESS: Cracked password found: '{password}'")
        break  # Stop the loop immediately once cracked (efficiency)
else:
    # This 'else' block executes only if the loop finishes without hitting 'break'
    print("\nFAIL: Target hash was not cracked using the common password list.")

print("-" * 40)

# --- 3. WHILE LOOP ---
# Use Case: Network Monitoring/Polling (Checking a condition repeatedly)
# Task: Continuously check a system health flag until it reports 'OK' or the maximum retries are hit.

print("--- 3. WHILE LOOP (System Health Check Polling) ---")

system_status = "PENDING"
retries = 0
MAX_RETRIES = 5

while system_status != "OK" and retries < MAX_RETRIES:
    retries += 1
    print(f"Attempt {retries}: System status is '{system_status}'. Waiting 2 seconds...")
    
    # Simulate a check: assume the system becomes 'OK' on the 4th retry
    if retries == 4:
        system_status = "OK"
    
    # In a real script, you would include time.sleep(2) here

if system_status == "OK":
    print("\nSUCCESS: System status verified as 'OK'. Resuming normal operations.")
else:
    print(f"\nFAILURE: Max retries ({MAX_RETRIES}) exceeded. Status remains '{system_status}'. Escalating to Level 2 support.")

print("-" * 40)