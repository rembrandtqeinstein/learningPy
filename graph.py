import matplotlib.pyplot as plt
import datetime
import statistics
import numpy as np

start = datetime.datetime.strptime("06-05-2020", "%d-%m-%Y")
end = datetime.datetime.strptime("01-02-2021", "%d-%m-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
dl = list()

for date in date_generated:
    dl.append(date.strftime("%d-%m-%Y"))

# From the 7 of July onwards Oral check same temp

temp = [35.3, 35.3, 35.8, 35.5, 35.6, 35.2, 35.4, 35.7, 35, 35.7, 36.1, 35.8, 35.8, 35.3, 35.3,
        36.1, 36.0, 35.3, 35.9, 35.7, 36.0, 35.8, 36.3, 35.9, 35.7, 35.4, 35.3, 36.0, 35.5, 36.1,
        36.1, 35.8, 35.3, 35.3, 35.3, 35.3, 35.4, 36.0, 35.7, 35.4, 35.0, 35.8, 35.1, 35.3, 35.7,
        36.1,35.9, 35.7, 35.2, 35.9, 34.9, 35.7, 35.9, 36.0, 35.7, 35.8, 36.3, 36.2, 35.8, 36.3, 35.5, 36.4, 35.7, 36.6, 36.5, 36.3, 36.8, 36.1, 35.6, 36.4, 36.6, 36.4, 36.0, 36.8, 36.3, 36.8, 35.5, 36.5, 35.9, 36.3, 36.6, 36.3, 36.5, 36.4, 36.4, 36.2, 36.7, 36.7, 35.8, 36.0, 36.5, 36.4, 36.4, 36.6, 36.3, 36.4, 36.3, 36.3, 36.3, 36.3, 36.3, 36.6, 36.0, 36.2, 36.3, 36.3, 36.0, 36.5, 36.6, 36.5, 36.2, 36.8, 36.5, 36.4, 36.5, 36.3, 36.6, 36.4, 36.3, 35.9, 36.0, 36.1, 36.6, 36.0, 35.9, 36.1, 36.3, 36.3, 36.4, 36.6, 36.3, 35.9, 36.2, 35.9, 36.0, 36.5, 36.4, 36.1, 36.2, 36.0, 35.9, 35.8, 36.1, 35.6, 36.1, 36.3, 36.3, 36.4, 35.6, 35.8, 36.0, 35.9, 36.0, 36.1, 36.0, 36.3, 36.2, 36.1, 35.8, 35.8, 35.7, 35.8, 35.4, 35.5, 36.2, 36.1, 35.9, 35.8, 35.8, 36.2, 35.8, 35.5, 36.2, 35.7, 35.8, 36.4, 36.2, 36.3, 35.8, 36.2, 36.1, 36.0, 36.1, 36.1, 35.9, 36.1, 36.2, 36.2, 36.3, 35.8, 35.8, 36.0, 35.9, 36.1, 35.7, 35.7, 35.7, 35.7, 36.4, 36.1, 36.0, 36.1, 36.4, 36.0, 36.2, 36.2, 35.9, 35.8, 35.9, 35.9, 36.0, 35.9, 35.7, 35.9, 35.7, 36.0, 35.8, 36.3, 35.8, 35.7, 35.7, 35.5, 35.5, 36.0, 36.2, 35.7, 36.1, 36.1, 36.0, 36.4, 35.8, 35.6, 36.2, 36.3, 35.6, 35.9, 35.9, 35.4, 36.3, 36.5, 35.8, 36.3, 35.8, 35.6, 36.0, 36.3, 36.1, 36.7, 36.3, 35.9, 35.8, 35.9, 36.3, 35.7, 35.9, 36.2, 35.7, 36.1, 36.3, 36.1, 35.4, 35.8, 35.8, 35.8, 36.2, 35.9, 36.1, 36.0, 35.8, 35.8, 36.1]

counts = dict()
for x in temp:
    counts[x] = counts.get(x,0) + 1

for x,y in zip(dl,temp):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xticks(np.arange(0,10,1))
plt.yticks(np.arange(0,7,0.5))

plt.plot(dl, temp, 'bo-')
plt.show()

plt.hist(temp, bins=len(temp))
plt.show()

ord = sorted([(v,k) for k,v in counts.items()], reverse=True)

for k, v in ord:
    print(v, k)

print("Average temp rounded till {}".format(end))
print(round(statistics.mean(temp),1))
print("Median temp rounded till {}".format(end))
print(statistics.median(temp))