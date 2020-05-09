str = 'X-DSPAM-Confidence: 0.8475 '

pos = str.find(':')
numb = float(str[pos+1:])
pos2 = str.find('0')
numb2 = float(str[pos2:])
print(numb, type(numb))
print(numb2, type(numb2))

# String documentation https://docs.python.org/3.5/library/stdtypes.html#string-methods
print(str.replace('e','a'))
print(str.strip('X5-'))
#str.strip('X-')