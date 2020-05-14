fname = input('Enter a valid file name and extension: ')

try:
    fhandler = open(fname)
except:
    print('Not a valid file, try mbox-short.txt')
    quit()

hist = dict()

for line in fhandler:
    # This line varies with the condition From: is a sender From SPACE is commits, and so knowing the document is key
    if not line.startswith('From:'):
        continue
    words = line.split()
    # This saves into Words only a list of splitted Email based on the @
    words = words[1].split('@')
    hist[words[1]] = hist.get(words[1],0) + 1

print(hist)
bcount = None
bname = None

for v,k in hist.items():
    if bname == None or bcount < k:
        bcount = k
        bname = v
print(bname, bcount)