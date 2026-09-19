# Code - POST
# Sending data with requests.post()

import requests

# API endpoint where we want to send the data.
url = "https://jsonplaceholder.typicode.com/posts"

# Data we want to send to the API.
payload = {
    "userId": 101,
    "title": "UTHM CodeVerse",
    "body": "Learning REST APIs with Python",    
}

# Send the data as JSON using a POST request.
response = requests.post(url, json=payload)

# 201 means the resource was successfully created.
print(response.status_code)

# The server sends back the created post as JSON.
print(response.json())