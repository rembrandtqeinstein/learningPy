import requests
from bs4 import BeautifulSoup

resp = requests.get("https://www.infobae.com/america/")
soup = BeautifulSoup(resp.text, "html.parser")
headline = soup.select('div.headline')

for num, head in enumerate(headline,1):
    print(num, head.text)

#import urllib.request, urllib.parse, urllib.error
#from bs4 import BeautifulSoup
#import ssl

#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

#html = 'https://www.nytimes.com/'
#page = urllib.request.urlopen(html, context=ctx).read()
#soup = BeautifulSoup(page, 'html.parser')
#tags = soup('span')
#for x in tags:
#    print(x)

#import requests
#from bs4 import BeautifulSoup

#response = requests.get("https://www.nytimes.com/")
#soup = BeautifulSoup(response.text,"html.parser")

#posts = soup.select('section:not(section[data-testid="block-Briefings"]) article')
#for i, post in enumerate(posts, 1):
#    print('{: <4}{}'.format(str(i) + '.', post.find('h2').text))