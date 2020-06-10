str = input("Enter a long string to be reversed word by word: ")

def reverse_str(str):
    lis = str.split(" ")
    lis.reverse()
    res = ""
    for x in lis:
        res = res + x + " "
    print(res)

reverse_str(str)