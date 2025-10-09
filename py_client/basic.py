import requests

#endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"
get_response = requests.post(endpoint, json={"title": "title from API", "content": "Content form API", "price": "asdas"})
#print(get_response.text)
#print(get_response.json()["message"])
print("Status code:", get_response.status_code)
print(get_response.json())