import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter -')
# Read the entered URL
html = urllib.request.urlopen(url).read()
# Convert it to a String
fun = html.decode()

tot = 0

results = json.loads(fun)
#print(results['comments'])
for v in results['comments']:
    num = int(v['count'])
    tot = tot + num

print(tot, len(results['comments']))