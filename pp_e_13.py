steps = input("Enter how many steps into the Fibonacci you want to take: ")

try:
    steps = int(steps)
except:
    print("Not a number")

def fibo (step):
    lis = list()
    lis.append(1)
    for x in range(1,step):
        if x == 1:
            lis.append(1)
        else:
            lis.append(lis[x-2]+lis[x-1])
    print(lis)

fibo(steps)