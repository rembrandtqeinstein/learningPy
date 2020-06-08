num = input("Enter the number to check the divisors for: ")

try:
    num = int(num)
except:
    print("Not a number")

div = range(1,num)
lis = [x for x in div if num % x == 0]
print(*lis, sep='\n')

#for x in div:
#    if num % x == 0:
#        lis.append(x)
#    else:
#        continue

#print([y for x in lis])