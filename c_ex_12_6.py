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
#html = urllib.request.urlopen(url, context=ctx).read()
#soup = BeautifulSoup(html, 'html.parser')
pos = input('Enter a position: ')
count = input('Enter a count: ')
try:
    pos = int(pos)
    count = int(count)
except:
    print('Not numbers entered')
    quit()

# Retrieve all of the anchor tags
#currentPos = 0
#tags = soup('a')
#for tag in tags:
#    currentPos = currentPos + 1
#    if currentPos == pos and count > 0:
#        print(tag.get('href', None))
#        currentPos = 0
#        count = count - 1

while count > 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    currentPos = 0
    for tag in tags:
        currentPos = currentPos + 1
        if currentPos == pos:
            print(tag.get('href',None))
            url = tag.get('href',None)
            count = count - 1
            break
