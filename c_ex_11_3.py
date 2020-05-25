import re

fname = input("Please provide the name of the file with the extension: ")

try:
    fhandler = open(fname)
except:
    print("Bad file name, please input valid, like mbox-short.txt")
    quit()

sum = 0
count = 0

for line in fhandler:
    line = line.strip()
    if re.findall('[0-9]+', line):
        numb = re.split('[a-z /]',line)
        #print(numb)
        for n in numb:
            try:
                n = int(n)
                sum = sum + n
                count = count + 1
            except:
                continue
    else:
        continue

print(sum, count)
