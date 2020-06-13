file = open("nameslist.txt", 'r')
dic = dict()

for i in file:
    names = i.rstrip()
    dic[names] = dic.get(names, 0) + 1

print(dic)

ord = sorted([(v,k) for k,v in dic.items()], reverse=True)

for v,k in ord:
    print(k,v)

file2 = open("Training_01.txt", 'r')
dic2 = dict()

for i in file2:
    names = i.rstrip()
    names = i.split("/")
    dic2[names[2]] = dic2.get(names[2], 0) + 1

ord2 = sorted([(v,k) for k,v in dic2.items()], reverse=True)

print("---------------")
for v,k in ord2:
    print(k,v)