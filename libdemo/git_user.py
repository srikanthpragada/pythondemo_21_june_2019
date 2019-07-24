import requests

resp = requests.get("https://api.github.com/users/srikanthpragada")
if resp.status_code == 200:
    user = resp.json()
    print("Name    : ", user['name'])
    print("Company : ", user['company'])
    print("Blog    : ", user['blog'])
else:
    print("Sorry! User not found!")