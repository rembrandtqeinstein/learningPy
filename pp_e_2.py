number = input("Enter a number: ")
div = input("Enter the denominator: ")

try:
    number = int(number)
    div = int(div)
except:
    print("Not a number")

if number % div == 0:
    print(number, "is a multiple of", div)
else:
    print(number, "is NOT a multiple of", div)

if number % 2 == 0:
    if number % 4 == 0:
        print(number, "is divisible by 4")
    else:
        print(number, "is even")
else:
    print(number, "is not even")