import requests
from bs4 import BeautifulSoup

resp = requests.get("https://www.infobae.com/america/")
soup = BeautifulSoup(resp.text, "html.parser")
headline = soup.select('div.headline')
name = input("Enter the name of the file: ")
f = open(name + ".txt", "w")

for num, head in enumerate(headline,1):
    f.write("%d %s \n" % (num, head.text))
    print(num, head.text)

f.close()

