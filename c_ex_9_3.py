fname = input('Enter a valid file name and extension: ')

try:
    fhandler = open(fname)
except:
    print('Not a valid file, try mbox-short.txt')
    quit()

hist = dict()

for line in fhandler:
    if not line.startswith('From:'):
        continue
    words = line.split()
    hist[words[1]] = hist.get(words[1],0) + 1

print(hist)
bcount = None
bname = None

for v,k in hist.items():
    if bname == None or bcount < k:
        bcount = k
        bname = v
print(bname, bcount)