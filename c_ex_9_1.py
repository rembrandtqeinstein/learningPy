fname = input('Enter a valid file name and extension: ')

try:
    fhandler = open(fname)
except:
    print('Not a valid file, try mbox-short.txt')
    quit()

hist = dict()

for line in fhandler:
    if not line.startswith('From '):
        continue
    words = line.split()
    # This line just look for the 3rd word, which we know is the date, and adds to the dict if it's not there, and adds 1 wether it is there or not. This only works because the date is always in the second position
    hist[words[2]] = hist.get(words[2],0) + 1

print(hist)