import random

leng_1 = random.randint(1,100)
leng_2 = random.randint(1,100)

a = random.sample(range(1, 100), leng_1)
b = random.sample(range(1, 100), leng_2)

c = set(a) & set(b)
print(c)