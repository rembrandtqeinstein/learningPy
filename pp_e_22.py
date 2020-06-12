file = open("nameslist.txt", 'r')
dic = dict()

for i in file:
    names = i.rstrip()
    dic[names] = dic.get(names, 0) + 1

print(dic)

ord = sorted([(v,k) for k,v in dic.items()], reverse=True)

for v,k in ord:
    print(k,v)