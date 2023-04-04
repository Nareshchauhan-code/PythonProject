import requests

dd = requests.get("https://reqres.in/api/users?page=2")
print(dd)
