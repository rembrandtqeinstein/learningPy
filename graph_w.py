import matplotlib.pyplot as plt
import datetime
import statistics
import numpy as np

start = datetime.datetime.strptime("07-07-2020", "%d-%m-%Y")
end = datetime.datetime.strptime("26-07-2020", "%d-%m-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
dl = list()

for date in date_generated:
    dl.append(date.strftime("%d-%m-%Y"))

weight = [67.1, 66.8, 66.8, 66.5, 66.7, 67.6, 68.2, 67.5, 67.8, 67.9, 67.5, 68.0, 67.4, 68.6, 68.0, 68.0, 68.5, 67.8, 68.4]

counts = dict()
for x in weight:
    counts[x] = counts.get(x,0) + 1

for x,y in zip(dl,weight):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xticks(np.arange(0,10,1))
plt.yticks(np.arange(0,7,0.5))

plt.plot(dl, weight, 'bo-')
plt.show()

plt.hist(weight, bins=len(weight))
plt.show()

ord = sorted([(v,k) for k,v in counts.items()], reverse=True)

for k, v in ord:
    print(v, k)

print("Average weight rounded till {}".format(end))
print(round(statistics.mean(weight),1))
print("Median weight rounded till {}".format(end))
print(round(statistics.median(weight),1))