import random

while True:
    count = 0
    num = random.randrange(1,10)
    guess = None
    while guess == None:
        gs = input("Guess a number from 1 to 9: ")
        if gs == 'exit':
            exit()
        try:
            gs = int(gs)
        except:
            print("Not a number")
        #if gs > 9 or gs < 1:
        #    print("Number out of range")
        count = count + 1
        if gs == num:
            guess = True
            print(gs, "is the number. You guessed on your", count)
        elif gs > num:
            print(gs, "is higher than the number")
        elif gs < num:
            print(gs, "is lower than the number")