# General form of Dicts to create Counts

counts = dict()
names = ['csev', 'cwen','csev','zqian','cwen']
for name in names:
    counts[name] = counts.get(name,0) + 1
print(counts)