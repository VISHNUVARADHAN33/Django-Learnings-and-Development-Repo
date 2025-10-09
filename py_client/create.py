import requests

endpoint = "http://localhost:8000/api/products/" 


data = {
    "title": "Iphone 17",
    "price": "200000",
    "content": "Content for iphone 17"
}
get_response = requests.post(endpoint, json=data) 
print(get_response.json())