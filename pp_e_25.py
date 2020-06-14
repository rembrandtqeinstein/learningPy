user_num = (int(input("Please think of a number between 0 and 100: ")))
low = 0
high = 100
ans = (high + low) // 2

while True:
    print("is your secret number " + str(ans))
    check_ans = input("""
    enter 'h' to indicate if the guess is too high.
    enter 'l' to indicate if the guess is too low.
    enter 'c' if I guessed correctly: 
    
    """)

    if check_ans == 'h':
        high = ans
        ans = (high + low) // 2
    elif check_ans == 'l':
        low = ans
        ans = (high + low) // 2
    elif check_ans == 'c' and ans == user_num:
        print("Game over. Your secret number was: " + str(ans))
        quit()
    else:
        print("I do not understand your command")