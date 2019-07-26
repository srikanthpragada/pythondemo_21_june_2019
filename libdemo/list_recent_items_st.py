import requests
import sys
from bs4 import BeautifulSoup
import re
from datetime import datetime

td = datetime.today()
resp = requests.get("http://www.srikanthtechnologies.com/rss.xml")
if resp.status_code != 200:
    print("Sorry! Could not get details. Quitting..")
    sys.exit(0)

bs = BeautifulSoup(resp.text,"xml")
for item in bs.find_all("item"):
    try:
        pubDate = item.find('pubDate').text
        m = re.match('([A-Za-z, ]+)(\d+).(\w+).(\d+)', pubDate)
        pd = datetime.strptime(f"{m.group(2)}-{m.group(3)}-{m.group(4)}","%d-%b-%Y")
        diff = td - pd
        if  diff.days < 365:
            print(item.find('title').text.strip(' '))
    except:
        pass




