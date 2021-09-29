import requests

url = "http://127.0.0.1/5000/total"

response = requests.request("GET", url)
assert response.status_code in [200, 404]
