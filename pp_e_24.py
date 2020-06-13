def board(width, height):
    hor = " ---"
    ver = "|   "
    ver = (ver * width) + "|"
    height = height *2
    for x in range(1,height+2):
        if x % 2 != 0:
            print(hor*width)
        else:
            print(ver)

width = input("Enter the width of the board: ")
height = input("Enter the height of the board: ")

try:
    width = int(width)
    height = int(height)
except:
    print("Not a number")
    quit()

board(width,height)