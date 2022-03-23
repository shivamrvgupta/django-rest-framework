from email import header
import json
import requests
 
header = {
    'Authorization' : 'Bearer af7366d6281b2b7d564e18b1b3fc6685be072be5'
}

endpoint = "http://127.0.0.1:8000/api/products/"    


data = {
    'title' : "This Field is Done",
    'price' : 32.99
}
get_response = requests.post(endpoint, json=data, headers=header)

print(get_response.json()) 
