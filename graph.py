import matplotlib.pyplot as plt
import datetime
import numpy as np

start = datetime.datetime.strptime("06-05-2020", "%d-%m-%Y")
end = datetime.datetime.strptime("25-06-2020", "%d-%m-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
dl = list()

for date in date_generated:
    dl.append(date.strftime("%d-%m-%Y"))

temp = [35.3, 35.3, 35.8, 35.5, 35.6, 35.2, 35.4, 35.7, 35, 35.7, 36.1, 35.8, 35.8, 35.3, 35.3,
        36.1, 36.0, 35.3, 35.9, 35.7, 36.0, 35.8, 36.3, 35.9, 35.7, 35.4, 35.3, 36.0, 35.5, 36.1,
        36.1, 35.8, 35.3, 35.3, 35.3, 35.3, 35.4, 36.0, 35.7, 35.4, 35.0, 35.8, 35.1, 35.3, 35.7,
        36.1,35.9, 35.7, 35.2,35.9]

counts = dict()
for x in temp:
    counts[x] = counts.get(x,0) + 1

plt.plot(dl, temp)
plt.show()

plt.hist(temp, bins=len(temp))
plt.show()

ord = sorted([(v,k) for k,v in counts.items()], reverse=True)

for k, v in ord:
    print(v, k)