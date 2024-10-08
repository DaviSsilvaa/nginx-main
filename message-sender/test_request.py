import requests

url = 'http://message-receiver:5000/receive'
data = {'message': 'Davi Silva dos Santos'}

response = requests.post(url, json=data)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
