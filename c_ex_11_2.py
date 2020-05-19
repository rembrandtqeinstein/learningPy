import re

fname = input("Please provide the name of the file with the extension: ")

try:
    fhandler = open(fname)
except:
    print("Bad file name, please input valid, like mbox-short.txt")
    quit()
total = 0
count = 0

for line in fhandler:
    line = line.rstrip()
    if re.findall('^New Revision: ', line):
        numb = line.split(':')
        numb = int(numb[1])
        total = total + numb
        count = count + 1
    else:
        continue
print(int(total/count))

#Find New Revision: 39766
#Sum and average the number
