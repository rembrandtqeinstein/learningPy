import random

def first_last (x):
    final = list()
    final.append(x[0])
    final.append(x[-1])
    print(final)

leng_1 = random.randint(1,100)
a = random.sample(range(1, 100), leng_1)

print(a)
first_last(a)