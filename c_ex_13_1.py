import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter -')
# Read the entered URL
html = urllib.request.urlopen(url).read()
fun = html.decode()

tot = 0

tree = ET.fromstring(fun)
results = tree.findall('.//count')
for n in results:
    count = int(n.text)
    tot = tot + count
print(tot, len(results))