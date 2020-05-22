import urllib.request, urllib.parse, urllib.error

fhand2 = urllib.request.urlopen('http://data.pr4e.org/intro.txt')
count = 0

for line2 in fhand2:
    words = line2.decode().split()
    for word in words:
        for ch in word:
            count = count + 1
print(count)
