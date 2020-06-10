num = input("Enter a number to check if it's a prime: ")

try:
    num = int(num)
except:
    print("Not a number")

def prime(x):
    div = range(1, x)
    lis = [y for y in div if x % y == 0]
    if len(lis) == 1:
        print(x, "is a prime number")
    else:
        print(x, "is not a prime number, it's divisible by", *lis)

prime(num)