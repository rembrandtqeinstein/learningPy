# Loop Exercise
# Exercise 1: Write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
numb = 0
suma = 0
count = 0
while numb != 'done':
    numb = input('Enter a number: ')
    # This IF Statement could be removed from the code, just to save a loop is placed here
    if numb == 'done':
        break
    try:
        numb = int(numb)
    except:
        print('bad data')
    if type(numb) == int:
        suma = suma + numb
        count+=1

print(suma, count, (suma/count))

# Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

small = None
big = None
numb2 = 0
while numb2 != 'done':
    numb2 = input('Enter a number: ')
    # This IF Statement could be removed from the code, just to save a loop is placed here
    if numb2 == 'done':
        break
    try:
        numb2 = int(numb2)
    except:
        print('bad data')
    if type(numb2) == int:
        if small is None:
            small = numb2
        if big is None:
            big = numb2
        elif numb2 < small:
            small = numb2
        elif numb2 > big:
            big = numb2

print(big, small)

# Finding the Smallest Number
smallest = None # Start with a None which helps not to initialize with a random number, the feeded list can be bigger
for i in [9,41,15,3,74,7]:
    if smallest is None:
        smallest = i
    elif i < smallest:
        smallest = i