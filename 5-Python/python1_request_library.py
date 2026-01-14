import requests 
response = requests.get("https://google.com")
print(f"Status Code: {response.status_code}")
if response.status_code != 200:
    print("Web security check failed.")