fname = input("Please provide the name of the file with the extension: ")

try:
    fhandler = open(fname)
except:
    print("Bad file name, please input valid, like mbox-short.txt")
    quit()

hist = dict()

for line in fhandler:
    line = line.rstrip()
    words = line.split()
    for w in words:
        w = w.lower()
        for ch in w:
            if ch.isalpha():
                hist[ch] = hist.get(ch,0) + 1

#print(hist)
ord = sorted([(v,k) for k,v in hist.items()], reverse=True)

for v,k in ord:
    print(k,v)