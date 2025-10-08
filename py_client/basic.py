import requests

endpoint = "https://httpbin.org/anything"
get_response = requests.get(endpoint, json={"question": "How are you?"})
print(get_response.text)