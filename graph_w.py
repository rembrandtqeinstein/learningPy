import matplotlib.pyplot as plt
import datetime
import statistics

start = datetime.datetime.strptime("07-07-2020", "%d-%m-%Y")
end = datetime.datetime.strptime("08-07-2020", "%d-%m-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
dl = list()

for date in date_generated:
    dl.append(date.strftime("%d-%m-%Y"))

weight = [67.1,]

counts = dict()
for x in weight:
    counts[x] = counts.get(x,0) + 1

plt.plot(dl, weight)
plt.show()

plt.hist(weight, bins=len(weight))
plt.show()

ord = sorted([(v,k) for k,v in counts.items()], reverse=True)

for k, v in ord:
    print(v, k)

print("Average temp rounded till {}".format(end))
print(round(statistics.mean(weight),1))
print("Median temp rounded till {}".format(end))
print(statistics.median(weight))