import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter -')
# Read the entered URL
html = urllib.request.urlopen(url).read()
# Convert it to a String
fun = html.decode()

tot = 0
# Get the Tree Object from the String
tree = ET.fromstring(fun)
# Find all the Counts in the XML
results = tree.findall('.//count') # I can't use .text here, because this is a list, there are several counts
for n in results:
    # Here I can use the .text because I'm iterating
    count = int(n.text)
    tot = tot + count
print(tot, len(results))