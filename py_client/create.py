import requests

endpoint = "http://localhost:8000/api/products/" 


data = {
    "title": "Item10",
    "price": "200000",
    "content": "Content for item1"
}
get_response = requests.post(endpoint, json=data) 
print(get_response.json())