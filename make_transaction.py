import requests
import json

url = "http://localhost:5000/transactions/new"

data = {
    "sender": "d4ee26eee15148ee92c6cd394edd974e",
    "recipient": "918e217ef4624b93af418124db3281c6",
    "amount": 5
}

headers = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.status_code)
print(response.json()) 
