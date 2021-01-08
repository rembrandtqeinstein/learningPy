import matplotlib.pyplot as plt
import datetime
import statistics
import numpy as np

start = datetime.datetime.strptime("07-07-2020", "%d-%m-%Y")
end = datetime.datetime.strptime("08-01-2021", "%d-%m-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
dl = list()

for date in date_generated:
    dl.append(date.strftime("%d-%m-%Y"))

# Lunes 26 Nada (Strings), Martes 27 Nada (Strings)

weight = [67.1, 66.8, 66.8, 66.5, 66.7, 67.6, 68.2, 67.5, 67.8, 67.9, 67.5, 68.0, 67.4, 68.6, 68.0, 68.0, 68.5, 67.8, 68.4, 69.0, 69.9, 68.9, 69.4, 67.9, 67.9, 68.6, 69.0, 69.2, 68.7, 68.7, 69.2, 68.1, 68.1, 69.0, 68.4, 68.0, 69.2, 68.1, 68.1, 68.1, 68.1, 69.2, 69.8, 69.5, 70.2, 69.3, 69.4, 69.6, 69.7, 69.2, 69.7, 68.9, 68.9, 68.8, 69.6, 69.9, 69.5, 69.3, 69.8, 68.9, 68.8, 68.8, 69.8, 69.4, 68.9, 69.7, 68.8, 68.8, 69.8, 69.8, 69.4, 69.0, 68.4, 68.7, 68.7, 68.7, 69.2, 69.2, 68.8, 68.7, 68.6, 68.3, 69.2, 69.6, 69.7, 69.1, 69.6, 70.0, 69.5, 70.1, 69.9, 69.9, 69.9, 69.3, 69.2, 69.2, 69.2, 70.0, 70.0, 69.2, 69.2, 68.9, 69.8, 70.4, 70.0, 69.1, 68.7, 69.3, 70.0, 69.0, 69.0, 69.5, 69.5, 69.1, 68.5, 68.8, 69.9, 70.7, 70.4, 69.4, 69.4, 69.4, 69.4, 69.4, 69.9, 70.4, 70.8, 69.6, 69.1, 68.6, 69.9, 69.9, 71.2, 70.0, 69.6, 69.6, 69.0, 70.4, 70.0, 70.7, 69.4, 69.4, 68.6, 68.9, 69.8, 70.8, 69.0, 69.0, 69.0, 69.8, 70.8, 69.9, 70.2, 70.0, 69.7, 69.7, 70.1, 70.1, 70.1, 70.1, 69.5, 70.1, 69.4, 69.9, 70.1, 70.7, 70.4, 70.4, 70.4, 71.1, 70.7, 71.4, 71.4, 71.1, 70.7, 71.4, 71.4, 70.9, 71.7, 71.7, 70.3, 70.3, 69.8, 69.8, 69.4]

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