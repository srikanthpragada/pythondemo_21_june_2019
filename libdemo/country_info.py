import requests
import sys
code = input("Enter country code :")

resp = requests.get(r"https://restcountries.eu/rest/v2/alpha/" + code)
if resp.status_code == 404:
  print("Sorry! Country code not found!")
  sys.exit(0)
elif resp.status_code != 200:
  print("Sorry! Could not get country details!")
  sys.exit(0)


details = resp.json()
print("Name : " + details["name"])
print("Capital : " + details["capital"])
print("Population : " + str(details["population"]))
print("Borders :")
for c in details["borders"]:
  print(c)

print("Currencies:")

for cur in details["currencies"]:
    print(cur['name'])