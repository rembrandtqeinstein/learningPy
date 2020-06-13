file = open("primenumbers.txt", 'r')
file2 = open("happynumbers.txt", 'r')

prime = list()
happy = list()

for x in file:
    num = x.rstrip()
    num = int(x)
    prime.append(num)

for y in file2:
    num = y.rstrip()
    num = int(y)
    happy.append(num)

#print(happy)
#print(prime)
joint = set(prime) & set(happy)

print(sorted(joint))