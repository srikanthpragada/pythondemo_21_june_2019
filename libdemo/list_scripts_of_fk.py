import requests
import sys
from bs4 import BeautifulSoup

resp = requests.get("https://www.flipkart.com")
if resp.status_code != 200:
    print("Sorry! Could not get details. Quitting..")
    sys.exit(0)

bs = BeautifulSoup(resp.text,"html.parser")
for link in bs.find_all("a"):
    if link['href'] != '#':
        print(link['href'] )


