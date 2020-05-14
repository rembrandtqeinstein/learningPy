fname = input('Enter a valid file name and extension: ')

try:
    fhandler = open(fname)
except:
    print('Not a valid file, try mbox-short.txt')
    quit()

hist = dict()

for line in fhandler:
    # This line works for the Sender FROM: looks at sender of the email
    if not line.startswith('From:'):
        continue
    words = line.split()
    # This only works because we know emails are on the second position
    hist[words[1]] = hist.get(words[1],0) + 1

print(hist)