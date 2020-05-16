fname = input("Please provide the name of the file with the extension: ")

try:
    fhandler = open(fname)
except:
    print("Bad file name, please input valid, like mbox-short.txt")
    quit()

hist = dict()

for line in fhandler:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    hist[words[1]] = hist.get(words[1],0) + 1

#print(hist)

lis = list()
for k,v in hist.items():
    tup = (v,k)
    lis.append(tup)

lis = sorted(lis, reverse=True)
#print(lis[0])

bcou, bnam = lis[0]
print(bnam,bcou)