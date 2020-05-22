# This files does the same as Socket with an external library to handle the stuff
import urllib.request, urllib.parse, urllib.error

# This is like the file open handler, opens the file, doesn't read it, just opens a channel. This allows us to treat the site like a file, so we can construct for loops to work around it
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# Reads the file from the handler, and since it's bytes we need to decode the line
for line in fhand:
    # This doesn't show the headers, there is a particular method for that
    print(line.decode().strip())


fhand2 = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line2 in fhand2:
    # We have to decode it from byte to string before we can process it, this is important. This turns to string so we can work with string methods.
    words = line2.decode().split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
print(counts)