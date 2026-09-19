# Code - GET
# Fetching data with requests.get()

import requests

# API endpoint we want to request.
url = "https://jsonplaceholder.typicode.com/posts/1"

# Send a GET request to the API.
response = requests.get(url)

print(response)

# Check the HTTP status code.
# 200 means the request was successful.
print(response.status_code)

# Check the type of data returned by the server.
print(response.headers["Content-Type"])

# Convert the JSON response into a Python dictionary.
data = response.json()
print(data)
# Access values from the dictionary using their keys.
print(data["title"])
print('--------------')
print(data["body"])