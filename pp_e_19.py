import requests
from bs4 import BeautifulSoup
import textwrap

resp = requests.get("http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture")
soup = BeautifulSoup(resp.text, "html.parser")
headline = soup.select('div.grid')

for line in headline:
    str = line.text
    my_wrap = textwrap.TextWrapper(width=140)
    print('\n\n' + my_wrap.fill(text=str))
    #for l in str:
    #    print(l)