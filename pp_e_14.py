import random

leng_1 = random.randint(1,50)
a = list()
for x in range(0, leng_1):
    a.append(random.randint(1,20))

def remove_duplicates(x):
    c = list(set(x))
    print(c)

def remove_duplicates_for(x):
    n_lis = list()
    for y in x:
        if y not in n_lis:
            n_lis.append(y)
        else:
            continue
    print(n_lis)

print(a)
remove_duplicates(a)
remove_duplicates_for(a)