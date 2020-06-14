winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

def winner(lis):
    # Vertical
    if lis[0][0] == lis[1][0] == lis[2][0] & (lis[0][0] or lis[1][0] or lis[2][0]) != 0:
        print(lis[0][0], "Wins. Vertical 1")
    elif lis[0][1] == lis[1][1] == lis[2][1] & (lis[0][1] or lis[1][1] or lis[2][1]) != 0:
        print(lis[0][1], "Wins. Vertical 2")
    elif lis[0][2] == lis[1][2] == lis[2][2] & (lis[0][2] or lis[1][2] or lis[2][2]) != 0:
        print(lis[0][2], "Wins. Vertical 3")
    # Horizontal
    elif lis[0][0] == lis[0][1] == lis[0][2] & (lis[0][0] or lis[0][1] or lis[0][2]) != 0:
        print(lis[0][0], "Wins. Horizontal 1")
    elif lis[1][0] == lis[1][1] == lis[1][2] & (lis[1][0] or lis[1][1] or lis[1][2]) != 0:
        print(lis[1][0], "Wins. Horizontal 2")
    elif lis[2][0] == lis[2][1] == lis[2][2] & (lis[2][0] or lis[2][1] or lis[2][2]) != 0:
        print(lis[2][0], "Wins. Horizontal 3")
    # Diagonal
    elif lis[0][0] == lis[1][1] == lis[2][2] & (lis[0][0] or lis[1][1] or lis[2][2]) != 0:
        print(lis[0][0], "Wins. Diagonal 1")
    elif lis[0][2] == lis[1][1] == lis[2][0] & (lis[0][2] or lis[1][1] or lis[2][0]) != 0:
        print(lis[0][2], "Wins. Diagonal 2")
    else:
        print("No winner, tied game")


winner(winner_is_2)
winner(winner_is_1)
winner(winner_is_also_1)
winner(no_winner)
winner(also_no_winner)
