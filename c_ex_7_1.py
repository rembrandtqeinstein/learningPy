fname = input('Enter file name and extension: ')

try:
    fhand = open(fname)
except:
    print('Bad file or Bad file Name')
    quit()

for line in fhand:
    line = line.rstrip()
    print(line.upper())