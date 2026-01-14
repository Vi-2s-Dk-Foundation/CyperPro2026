import os

# --- Configuration for Demo ---
LOG_FILE_NAME = "web_access_log.txt"
CONFIG_FILE_NAME = "security_config.ini"
HASH_LIST_NAME = "malicious_hashes.txt"

def write_and_read_log_data():
    """Demonstrates writing log data (simulating a Web Access Log) and then reading it."""
    log_data = [
        "192.168.1.10 - [20/Jan/2025:09:00:01] \"GET /index.html\" 200",
        "10.0.0.5 - [20/Jan/2025:09:00:02] \"POST /login\" 401",
        "172.16.0.22 - [20/Jan/2025:09:00:03] \"GET /admin/users.php\" 403",
        "192.168.1.10 - [20/Jan/2025:09:00:05] \"GET /assets/style.css\" 200"
    ]

    print("--- 1. Writing New Access Log Data (Mode 'w') ---")
    try:
        # Use 'w' (write mode) to create or overwrite the file
        with open(LOG_FILE_NAME, 'w') as f:
            for line in log_data:
                f.write(line + '\n')
        print(f"Successfully wrote {len(log_data)} lines to {LOG_FILE_NAME}.")

        print("\n--- 2. Reading Log Data (Mode 'r') ---")
        # Use 'r' (read mode) to read the entire file content
        with open(LOG_FILE_NAME, 'r') as f:
            content = f.read()
            print(content)

    except IOError as e:
        print(f"An error occurred during file operation: {e}")

def append_to_hash_list():
    """Demonstrates appending new threat intelligence data (hashes) to an existing list."""
    new_hashes = [
        "5a6e7b8c9d0f1a2b3c4d5e6f7a8b9c0d",  # Known malware
        "f0e9d8c7b6a54e3d2c1b0a9f8e7d6c5b"   # New suspicious file
    ]
    
    # Ensure the file exists before appending, or create it if it doesn't
    # Initial setup: create an empty or minimal hash list
    with open(HASH_LIST_NAME, 'w') as f:
        f.write("# Malicious Hashes List\n")

    print("\n--- 3. Appending New Hashes (Mode 'a') ---")
    try:
        # Use 'a' (append mode) to add data without overwriting existing content
        with open(HASH_LIST_NAME, 'a') as f:
            for h in new_hashes:
                f.write(h + '\n')
        print(f"Successfully appended {len(new_hashes)} hashes to {HASH_LIST_NAME}.")

        print("\n--- 4. Reading Appended Data Line by Line ---")
        # Reading line by line is crucial for large files like log/hash lists
        with open(HASH_LIST_NAME, 'r') as f:
            print(f"Content of {HASH_LIST_NAME}:")
            for line in f:
                print(f" > {line.strip()}")

    except IOError as e:
        print(f"An error occurred during file operation: {e}")

def handle_config_file_error():
    """Demonstrates error handling when attempting to read a binary file as text."""
    
    # Create a simulated binary file (e.g., encrypted config) that should not be read as text
    binary_data = b'\xfe\xed\xfa\xce\xde\xad\xbe\xef'
    with open(CONFIG_FILE_NAME, 'wb') as f:
        f.write(binary_data)
        
    print("\n--- 5. Demonstrating Error Handling (Reading Binary as Text) ---")
    try:
        # Attempt to read a binary file using text mode ('r')
        with open(CONFIG_FILE_NAME, 'r') as f:
            f.read()
        
    except UnicodeDecodeError:
        print(f"Caught expected error: UnicodeDecodeError when reading {CONFIG_FILE_NAME} in text mode.")
        print("Reason: The file contains non-text (binary) data.")
        
    except Exception as e:
        print(f"Caught an unexpected error: {e}")
        
    finally:
        # Cleanup created files
        if os.path.exists(LOG_FILE_NAME):
            os.remove(LOG_FILE_NAME)
        if os.path.exists(HASH_LIST_NAME):
            os.remove(HASH_LIST_NAME)
        if os.path.exists(CONFIG_FILE_NAME):
            os.remove(CONFIG_FILE_NAME)
        print("\nCleanup complete. Temporary files removed.")

if __name__ == "__main__":
    write_and_read_log_data()
    append_to_hash_list()
    handle_config_file_error()