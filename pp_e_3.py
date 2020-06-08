lis = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
top = input("Enter Max Number: ")

try:
    top = int(top)
except:
    print("Not a number entered")

n_lis = [x for x in lis if x < top]

#for x in lis:
#    if x < top:
#        n_lis.append(x)
#    else:
#        continue
for x in n_lis:
    print(x)