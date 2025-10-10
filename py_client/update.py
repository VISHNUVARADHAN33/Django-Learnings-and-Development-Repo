import requests

endpoint = "http://localhost:8000/api/products/1/update/" 
data = {
    'title': 'new item1',
    'price': 15556
}
get_response = requests.put(endpoint, json= data) 
print(get_response.json())