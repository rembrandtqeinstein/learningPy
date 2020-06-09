import random

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

lis1 = random.sample(range(0,100), 50)
lis2 = random.sample(range(0,100), 50)

c = set(lis1) & set(lis2)  #  & calculates the intersection.
lis = list(c)
print(lis)