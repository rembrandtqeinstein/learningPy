flist = list()
while True:
    numb = input("Say a number: ")
    if numb == 'done': break
    try:
        numb = float(numb)
    except:
        print('Its not a number')
        continue
    flist.append(numb)

print('Max number inputted',max(flist))
print('Min number inputted',min(flist))