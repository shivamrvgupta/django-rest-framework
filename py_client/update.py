import json
import requests
 
endpoint = "http://127.0.0.1:8000/api/products/1/update/"    

data = {
    "title" : "hello wolrd my old friend",
    "price" : 199.00
}

get_response = requests.put(endpoint, json=data)

print(get_response.json()) 
