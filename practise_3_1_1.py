import requests, json

base_url = "http://127.0.0.1:5000"

response = requests.post(f"{base_url}/drone/takeoff")
print(f"Status code: {response.status_code}")
print(response.json())
