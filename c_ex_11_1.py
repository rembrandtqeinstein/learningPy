import re
fhandler = open('mbox.txt')

regex = input('Please input your RegEx to search in mbox: ')

#if re.error(regex):
#    quit()
#else:
#    print('Sucess')

# Regex to try ^X- ^Author java$
count = 0
for line in fhandler:
    line = line.rstrip()
    if re.findall(regex, line):
        count = count + 1
    else:
        continue
print('mbox.txt had',count, 'lines that matched', regex)
