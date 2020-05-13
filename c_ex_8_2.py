fname = input("Please provide the name of the file with the extension: ")

try:
    fhandler = open(fname)
except:
    print("Bad file name, please input valid, like mbox-short.txt")
    quit()

count = 0

for line in fhandler:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    line = line.split()
    print(line[1])
    count = count + 1

print('There were',count,'lines in the file that started with From')