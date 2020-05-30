import urllib.request, urllib.parse, urllib.error
import json

while True:
    serviceurl = input('Enter -')
    if len(serviceurl) < 1: break

    parms = dict()
    token = input('Enter your Token -')
    parms['token'] = token

    url = serviceurl + '?' + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    print(json.dumps(js, indent=4)) # Print the JSON

    for k in js['civilizations']:
        print(k)
        print(k['name'])