'''import string
from random import choice

while True:
    chars = string.digits
    num =  ''.join(choice(chars) for _ in range(4))
    print(num)
    guess = False
    while guess == False:
        gs = input("Enter 4 digits number to guess (done to exit): ")
        if gs == 'done':
            quit()
        else:
            if gs == num:
                print("Guessed", gs, num)
                guess = True
            else:
                c = set(gs) & set(num)
                print(c)
'''

import random

def game(num_digits):
    # generate list of random integers of length num_digits
    listnum = [random.randint(0,9) for n in range(num_digits)]
    #print("Solution key = " + str(listnum))

    count=0
    while True:
        count+=1
        print("~~~ Guess: " + str(count) + " ~~~")

        print("Please guess " + str(num_digits) + "-digit number: ")
        # transform input string (e.g. "1234") to list of integers (e.g. [1,2,3,4])
        guess = [int(i) for i in str(input())]

        if guess == listnum:
            print("You won.")
            print("It took you "+str(count)+" guess(es).")
            break

        else:
            cow=0
            bull=0

            for x in range(0,num_digits):
                if guess[x]==listnum[x]:
                    cow += 1
                elif guess[x] in listnum: # look if digit is somewhere else in the solution key (might already be a cow)
                    bull += 1

        print("Cows: "+str(cow)+" Bulls: "+str(bull))
        print("++++++++++++++++")

game(4)