import requests
import json

url = "http://127.0.0.1:8000/user/"


data = {
    'First_name': 'Kanchan',
    'Last_name': 'Sharma',
    'City': 'Noida',
    'Pincode': 203209,
    'Phone_No': 1234567890
}

# convert into python native object

json_data = json.dumps(data)

# post request

r = requests.post(url=url, data=json_data)

data = r.json()
print(data)
