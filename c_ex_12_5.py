# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('span')
count = list()
#countt = 0
#total = 0
for tag in tags:
    for v in tag:
        try:
            v = int(v)
        except:
            continue
        count.append(v)
        #countt = countt + 1
        #total = total + v

tot = sum(count)
leng = len(count)
print("Sum:",tot, "Amount of N°:", leng, "Average:",tot/leng)
#print(leng)
#print(tot/leng)

#print(countt)
#print(total)

