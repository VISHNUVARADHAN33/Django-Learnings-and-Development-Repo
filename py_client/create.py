import requests
headers = {'Authorization':'Bearer 48faffdd13ffb6b80c8fa29d630cad0329e16da0'}
endpoint = "http://localhost:8000/api/products/" 


data = {
    "title": "Item10",
    "price": "200000",
}
get_response = requests.post(endpoint, json=data, headers=headers) 
print("Status Code:", get_response.status_code)
print(get_response.json())