import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter -')
# Read the entered URL
html = urllib.request.urlopen(url).read()
# Corrects and parses the HTML mess
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all the anchor tags and print the URLs
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))