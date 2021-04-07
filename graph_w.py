import matplotlib.pyplot as plt
import datetime
import statistics
import numpy as np

start = datetime.datetime.strptime("07-07-2020", "%d-%m-%Y")
end = datetime.datetime.strptime("07-04-2021", "%d-%m-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
dl = list()

for date in date_generated:
    dl.append(date.strftime("%d-%m-%Y"))

# Domingo 10 Nada, Lunes 11 Nada, Martes 12 Si Verde, Miercoles 13 Si, Jueves 14 x2, Viernes 15 x2, Sabado 16 Si, Domingo 17 Nada, Lunes 18 Si Pelotita Verde, Martes 19 x2, Miercoles 20 Si, Jueves 21 si, Viernes 22 si, Sabado 23 Nada, Domingo 24 Si, Lunes 25 Si x 3 Verde, Martes 26 Si Verde, Miercoles 27 Si x2, Jueves 28 Si x2, Viernes 29 Si, Sabado 30 Nada, Domingo 31 Pelotita Verde, Lunes 01 Si Verde, Martes 02 Si, Miercoles 03 Si, Jueves 04 Pelotitas, Viernes 05 Si x3 Sabado 06 Si, Domingo 07 Si, Lunes 08 Si x2, Martes 09 Si x2, Miercoles 10 Si, Jueves 11 Si, Viernes 12 Si x2, Sabado 13 Si, Domingo 14 Si, Lunes 15 Si Pelotitas verdes, Martes 16 Si, Miercoles 17 Si x2, Jueves 18 Si x2, Viernes 19 Si x2, Sabado 20 Si, Domingo 21 Si Verde, Lunes 22 Si, Martes 23 Si x2, Miercoles 24 Si x3, Jueves 25 Si, Viernes 26 Si, Sabado 27 Si, Domingo 28 Si, Lunes 01 Si, Martes 02 Si x2, Miercoles 03 Si, Jueves 04 Si x2, Viernes 05 Si x2, Sabado 06 No, Domingo 07 Si, Lunes 08 Si, Martes 09 Si, Miercoles 10 Si, Jueves 11 Si x2, Viernes 12 Si x2, Sabado 13 Si, Domingo 14 Si x2, Lunes 15 Si, Martes 16 Si x2, Miercoles 17 Si, Jueves 18 Si x2, Viernes 19 Si, Sabado 20 Si, Domingo 21 Si, Lunes 22 Si, Martes 23 Si x3, Miercoles 24 Si, Jueves 25 Si x2, Viernes 26 Si, Sabado 27 Si x2, Domingo 28 Si, Lunes 29 Si x2, Martes 30 Si, Miercoles 31 Si, Jueves 01 No, Viernes 02 Si x2, Sabado 03 Si, Domingo 04 Si, Lunes 05 Si, Martes 06 Si, Miercoles 07 Si

weight = [67.1, 66.8, 66.8, 66.5, 66.7, 67.6, 68.2, 67.5, 67.8, 67.9, 67.5, 68.0, 67.4, 68.6, 68.0, 68.0, 68.5, 67.8, 68.4, 69.0, 69.9, 68.9, 69.4, 67.9, 67.9, 68.6, 69.0, 69.2, 68.7, 68.7, 69.2, 68.1, 68.1, 69.0, 68.4, 68.0, 69.2, 68.1, 68.1, 68.1, 68.1, 69.2, 69.8, 69.5, 70.2, 69.3, 69.4, 69.6, 69.7, 69.2, 69.7, 68.9, 68.9, 68.8, 69.6, 69.9, 69.5, 69.3, 69.8, 68.9, 68.8, 68.8, 69.8, 69.4, 68.9, 69.7, 68.8, 68.8, 69.8, 69.8, 69.4, 69.0, 68.4, 68.7, 68.7, 68.7, 69.2, 69.2, 68.8, 68.7, 68.6, 68.3, 69.2, 69.6, 69.7, 69.1, 69.6, 70.0, 69.5, 70.1, 69.9, 69.9, 69.9, 69.3, 69.2, 69.2, 69.2, 70.0, 70.0, 69.2, 69.2, 68.9, 69.8, 70.4, 70.0, 69.1, 68.7, 69.3, 70.0, 69.0, 69.0, 69.5, 69.5, 69.1, 68.5, 68.8, 69.9, 70.7, 70.4, 69.4, 69.4, 69.4, 69.4, 69.4, 69.9, 70.4, 70.8, 69.6, 69.1, 68.6, 69.9, 69.9, 71.2, 70.0, 69.6, 69.6, 69.0, 70.4, 70.0, 70.7, 69.4, 69.4, 68.6, 68.9, 69.8, 70.8, 69.0, 69.0, 69.0, 69.8, 70.8, 69.9, 70.2, 70.0, 69.7, 69.7, 70.1, 70.1, 70.1, 70.1, 69.5, 70.1, 69.4, 69.9, 70.1, 70.7, 70.4, 70.4, 70.4, 71.1, 70.7, 71.4, 71.4, 71.1, 70.7, 71.4, 71.4, 70.9, 71.7, 71.7, 70.3, 70.3, 69.8, 69.8, 69.4, 69.4, 69.1, 69.4, 71.3, 69.5, 70.7, 69.9, 69.6, 69.6, 69.6, 69.9, 69.6, 69.0, 69.0, 69.0, 70.5, 70.0, 68.8, 69.2, 69.2, 68.5, 68.5, 69.5, 70.1, 69.5, 69.0, 69.5, 68.9, 68.9, 70.1, 70.1, 69.6, 69.6, 69.0, 69.0, 68.0, 69.7, 69.7, 69.7, 69.7, 69.0, 69.0, 69.2, 70.2, 69.8, 69.8, 69.1, 69.1, 69.7, 69.2, 70.0, 70.0, 69.5, 69.5, 69.0, 69.0, 68.6, 69.9, 70.0, 70.0, 69.4, 69.4, 69.4, 68.8, 69.2, 69.9, 69.2, 69.1, 69.1, 68.6, 70.1, 70.4, 70.4, 69.3, 68.6, 69.1, 69.8, 70.1, 70.2, 70.2, 69.4, 69.4, 70.1, 70.1, 70.3, 70.6, 69.8, 69.6, 69.5]

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