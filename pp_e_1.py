import datetime
now = datetime.datetime.now()
year = now.year
name = input("Please enter your name: ")
age = input("Please enter your age: ")
copies = input("How many times should I print the message?: ")

try:
    age = int(age)
    copies = int(copies)
except:
    print("The input on Age is not a number")

turn = (100 - age) + year

while copies > 0:
    print(name, "you will be 100 years in the year", turn)
    copies = copies - 1