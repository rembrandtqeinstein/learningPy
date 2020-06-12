import random

res = list()

def in_list(lis, num):
    leng_1 = random.randint(1, 100)
    lis = [random.randrange(1, 50, 1) for i in range(leng_1)]
    lis.sort()
    if num in lis:
        print(True)
    else:
        print(False)

while True:
    search = input("Enter a number to look for in the ramdon list, from 1 to 100 (done to exit): ")
    if search == 'done':
        quit()
    try:
        search = int(search)
    except:
        print("Not a number")
        quit()
    in_list(res,search)