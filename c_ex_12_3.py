
import urllib.request
import urllib.parse
import urllib.error


fhand = urllib.request.urlopen('http://data.pr4e.org/intro.txt')

characters = 0
for line in fhand:
    # \n is considered a character
    # Amend to line.decode().rstrip() if needed
    words = line.decode()
    characters = characters + len(words)
    if characters < 3000:
        print(line.decode().strip())
print(characters)