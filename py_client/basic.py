import requests

#endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api"
get_response = requests.get(endpoint,params={"abc": 123}, json={"question": "How are you? form py_client"})
#print(get_response.text)
#print(get_response.json()["message"])
print(get_response.json())