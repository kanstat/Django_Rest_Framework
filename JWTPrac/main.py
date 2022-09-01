# python application------------->>>>>>webapi

import requests
url = "http://127.0.0.1:8000/all"

r = requests.get(url=url)

data = r.json()
print(data)
