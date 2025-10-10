import requests

endpoint = "http://localhost:8000/api/products/" 


data = {
    "title": "Item10",
    "price": "200000",
}
get_response = requests.post(endpoint, json=data) 
print("Status Code:", get_response.status_code)
print(get_response.json())