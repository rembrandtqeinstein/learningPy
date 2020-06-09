
while True:
    inp1 = input("Player 1, Enter paper, rock or sissors (done to exit): ")
    if inp1 == 'done':
        break
    inp2 = input("Player 2, Enter paper, rock or sissors (done to exit): ")
    if inp2 == 'done':
        break

    if inp1 == 'paper' and inp2 == 'rock':
        print("Player 1 wins with", inp1, "over", inp2)
    elif inp1 == 'paper' and inp2 == 'sissors':
        print("Player 2 wins with", inp2, "over", inp1)
    elif inp1 == 'rock' and inp2 == 'sissors':
        print("Player 1 wins with", inp1, "over", inp2)
    elif inp1 == 'rock' and inp2 == 'paper':
        print("Player 2 wins with", inp2, "over", inp1)
    elif inp1 == "sissors" and inp2 == "paper":
        print("Player 1 wins with", inp1, "over", inp2)
    elif inp1 == "sissors" and inp2 == "rock":
        print("Player 2 wins with", inp2, "over", inp1)
    elif inp1 == inp2:
        print("Tied game", inp1, inp2)
    else:
        print("Someone entered a non valid move")

