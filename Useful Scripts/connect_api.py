import requests

url = "https://api.example.com/resource"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YourTokenHere"
}

# Example GET request
response = requests.get(url, headers=headers)

# Example POST request with data
data = {"key1": "value1", "key2": "value2"}
response_post = requests.post(url, json=data, headers=headers)

# Example of handling the response
if response.status_code == 200:
    print("Request successful!")
    print(response.json())
else:
    print(f"Error in request: {response.status_code}")
    print(response.text)