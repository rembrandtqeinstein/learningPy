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
    words = words[5].split(':')
    hist[words[0]] = hist.get(words[0],0) + 1
    #print(words)

#print(hist) # Added comment

# This for and order can be replaced with a single Line ORD Line to create a list of tuples organized by key and then print it one by one
#lis = list()
#for k,v in hist.items():
#    tup = (k,v)
#    lis.append(tup)

#lis= sorted(lis)
#for k,v in ord:
#    print(k, v)

ord = sorted([(k,v) for k,v in hist.items()])
#print(ord)

for k,v in ord:
    print(k, v)