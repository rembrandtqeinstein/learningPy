# This creates a handler not accessing the file but a way to access it
handler = open('mbox-short.txt')
print(handler)

# This line reads all the lines, included special characters like escape characters as one single string line
# fread = handler.read()

# Creates a For Loop that goes line by line of the file
for line in handler:
    # RStrip removes the New Line escape character from Python. All Print Functions add a New Line escape character when called, so this helps not to have a double new line
    line = line.rstrip()
    # Up until here is a basic and re usable code for file handling when text

    # This two If Statement do the same. They check for lines that start with From and then prints them, wihtout the additional New Line escape character from the file it self (Striped with rstrip).
    # Second If Statement is a bit more efficient, because it skips bad lines and reaches for good ones alone
    if line.startswith('From:'):
        print(line)
    if not line.startswith('From:'):
        # Skip back to the top of the loop, not doing the next print
        continue
    print(line)

# Good idea to have input from user for File Name and have a try and except
fname = input('Enter the file name with extension: ')

try:
    fhandler = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()