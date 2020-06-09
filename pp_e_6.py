str = input("Enter a string you want to check if it's a palindrome: ")
str = str.replace(" ", "")

lis = [c for c in str]
r_lis = [c for c in str]
r_lis.reverse()

count = 0

for x in range(0,len(lis)):
    if lis[x] == r_lis[x]:
        count = count + 1
    else:
        continue

if count == len(lis):
    print(str, "Is a palindrome")
else:
    print(str, "Is not a palindrome")