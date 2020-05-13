fname = input("Please provide the name of the file with the extension: ")

try:
    fhandler = open(fname)
except:
    print("Bad file name, please input valid, like romeo.txt")
    quit()

words = list()

for line in fhandler:
    line = line.rstrip()
    line = line.split()
    for word in line:
        if word not in words:
            words.append(word)
        else:
            continue

words.sort()
print(words)