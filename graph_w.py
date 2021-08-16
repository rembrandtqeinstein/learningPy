import matplotlib.pyplot as plt
import datetime
import statistics
import numpy as np

start = datetime.datetime.strptime("07-07-2020", "%d-%m-%Y")
end = datetime.datetime.strptime("16-08-2021", "%d-%m-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
dl = list()

for date in date_generated:
    dl.append(date.strftime("%d-%m-%Y"))

# Domingo 10 Nada, Lunes 11 Nada, Martes 12 Si Verde, Miercoles 13 Si, Jueves 14 x2, Viernes 15 x2, Sabado 16 Si, Domingo 17 Nada, Lunes 18 Si Pelotita Verde, Martes 19 x2, Miercoles 20 Si, Jueves 21 si, Viernes 22 si, Sabado 23 Nada, Domingo 24 Si, Lunes 25 Si x 3 Verde, Martes 26 Si Verde, Miercoles 27 Si x2, Jueves 28 Si x2, Viernes 29 Si, Sabado 30 Nada, Domingo 31 Pelotita Verde, Lunes 01 Si Verde, Martes 02 Si, Miercoles 03 Si, Jueves 04 Pelotitas, Viernes 05 Si x3 Sabado 06 Si, Domingo 07 Si, Lunes 08 Si x2, Martes 09 Si x2, Miercoles 10 Si, Jueves 11 Si, Viernes 12 Si x2, Sabado 13 Si, Domingo 14 Si, Lunes 15 Si Pelotitas verdes, Martes 16 Si, Miercoles 17 Si x2, Jueves 18 Si x2, Viernes 19 Si x2, Sabado 20 Si, Domingo 21 Si Verde, Lunes 22 Si, Martes 23 Si x2, Miercoles 24 Si x3, Jueves 25 Si, Viernes 26 Si, Sabado 27 Si, Domingo 28 Si, Lunes 01 Si, Martes 02 Si x2, Miercoles 03 Si, Jueves 04 Si x2, Viernes 05 Si x2, Sabado 06 No, Domingo 07 Si, Lunes 08 Si, Martes 09 Si, Miercoles 10 Si, Jueves 11 Si x2, Viernes 12 Si x2, Sabado 13 Si, Domingo 14 Si x2, Lunes 15 Si, Martes 16 Si x2, Miercoles 17 Si, Jueves 18 Si x2, Viernes 19 Si, Sabado 20 Si, Domingo 21 Si, Lunes 22 Si, Martes 23 Si x3, Miercoles 24 Si, Jueves 25 Si x2, Viernes 26 Si, Sabado 27 Si x2, Domingo 28 Si, Lunes 29 Si x2, Martes 30 Si, Miercoles 31 Si, Jueves 01 No, Viernes 02 Si x2, Sabado 03 Si, Domingo 04 Si, Lunes 05 Si, Martes 06 Si, Miercoles 07 Si, Jueves 08 Si, Viernes 09 Si x2, Sabado 10 No, Domingo 11 Si, Lunes 12 Si, Martes 13 Si, Miercoles 14 Si, Jueves 15 Si, Viernes 16 Si, Sabado 17 Si, Domingo 18 Si, Lunes 19 Si, Martes 20 Si, Miercoles 21 Si, Jueves 22 Si, Viernes 23 Si x2, Sabado 24 Si, Domingo 25 Si, Lunes 26 Si, Martes 27 Si, Miercoles 28 Si, Jueves 29 Si, Viernes 30 Si x2, Sabado 01 Si, Domingo 02 Si, Lunes 03 Si Pelotitas, Martes 04 Si, Miercoles 05 Si, Jueves 06 Si, Viernes 07 Si x2, Sabado 08 Si, Domingo 09 Si, Lunes 10 Si, Martes 11 Si x3, Miercoles 12 Si, Jueves 13 Si x2, Viernes 14 Si, Sabado 15 Si, Domingo 16 No, Lunes 17 Si x2, Martes 18 Si x2, Miercoles 19 Si, Jueves 20 Si (Rojo por Remolacha dia anterior) x2, Viernes 21 Si, Sabado 22 Si x2, Domingo 23 No, Lunens 24 Si, Martes 25 Si x2, Miercoles 26 Si, Jueves 27 Si, Viernes 28 Si x3, Sabado 29 Si, Domingo 30 Si, Lunes 31 Si x 2, Martes 1 Si x2, Miercoles 2 Si, Jueves 3 Si x2, Viernes 4 Si x2, Sabado 5 Si, Domingo 6 Si, Lunes 7 No, Martes 8 Si, Miercoles 9 Si, Jueves 10 Si, Viernes 11 Si x3, Sabado 12 Si, Domingo 13 No, Lunes 14 Si x2, Martes 15 Si x2, Miercoles 16 Si, Jueves 17 Si x3, Viernes 18 Si x2, Sabado 19 Si x2, Domingo 20 Si, Lunes 21 Si, Martes 22 Si x2, Miercoles 23 Si, Jueves 24 Si, Viernes 25 Si, Sabado 26 Si, Domingo 27 No, Lunes 28 Si x3, Martea 29 Si x2, Miercoles 30 Si, Jueves 01 Si, Viernes 02 Si x2, Sabado 03 Si x2, Domingo 04 No, Lunes 05 No, Martes 06 No, Miercoles 07 Si, Jueves 08 Si, Viernes 09 Si x2, Sabado 10 Si, Domingo 11 Si, Lunes 12 Si, Martes 13 Si, Miercoles 14 Si, Jueves 15 Si, Viernes 16 Si, Sabado 17 Si, Domingo 18 Si, Lunes 19 Si x2, Martes 20 Si, Miercoles 21 Si, Jueves 22 Si, Viernes 23 Si, Sabado 24 Si, Domingo 25 Si, Lunes 26 Si, Martes 27 Si x3, Miercoles 28 Si, Jueves 29 Si, Viernes 30 Si, Sabado 31 Si, Domingo 01 No, Lunes 02 Si, Martes 03 Si x2, Miercoles 04 Si, Jueves 05 Si, Viernes 06 Si, Sabado 07 Si, Domingo 08 Si, Lunes 09 Si, Martes 10 Si, Miercoles 11 Si, Jueves 12 Si, Viernes 13 Si, Sabado 14 Si, Domingo 15 Si, Lunes 16 Si x2

weight = [67.1, 66.8, 66.8, 66.5, 66.7, 67.6, 68.2, 67.5, 67.8, 67.9, 67.5, 68.0, 67.4, 68.6, 68.0, 68.0, 68.5, 67.8, 68.4, 69.0, 69.9, 68.9, 69.4, 67.9, 67.9, 68.6, 69.0, 69.2, 68.7, 68.7, 69.2, 68.1, 68.1, 69.0, 68.4, 68.0, 69.2, 68.1, 68.1, 68.1, 68.1, 69.2, 69.8, 69.5, 70.2, 69.3, 69.4, 69.6, 69.7, 69.2, 69.7, 68.9, 68.9, 68.8, 69.6, 69.9, 69.5, 69.3, 69.8, 68.9, 68.8, 68.8, 69.8, 69.4, 68.9, 69.7, 68.8, 68.8, 69.8, 69.8, 69.4, 69.0, 68.4, 68.7, 68.7, 68.7, 69.2, 69.2, 68.8, 68.7, 68.6, 68.3, 69.2, 69.6, 69.7, 69.1, 69.6, 70.0, 69.5, 70.1, 69.9, 69.9, 69.9, 69.3, 69.2, 69.2, 69.2, 70.0, 70.0, 69.2, 69.2, 68.9, 69.8, 70.4, 70.0, 69.1, 68.7, 69.3, 70.0, 69.0, 69.0, 69.5, 69.5, 69.1, 68.5, 68.8, 69.9, 70.7, 70.4, 69.4, 69.4, 69.4, 69.4, 69.4, 69.9, 70.4, 70.8, 69.6, 69.1, 68.6, 69.9, 69.9, 71.2, 70.0, 69.6, 69.6, 69.0, 70.4, 70.0, 70.7, 69.4, 69.4, 68.6, 68.9, 69.8, 70.8, 69.0, 69.0, 69.0, 69.8, 70.8, 69.9, 70.2, 70.0, 69.7, 69.7, 70.1, 70.1, 70.1, 70.1, 69.5, 70.1, 69.4, 69.9, 70.1, 70.7, 70.4, 70.4, 70.4, 71.1, 70.7, 71.4, 71.4, 71.1, 70.7, 71.4, 71.4, 70.9, 71.7, 71.7, 70.3, 70.3, 69.8, 69.8, 69.4, 69.4, 69.1, 69.4, 71.3, 69.5, 70.7, 69.9, 69.6, 69.6, 69.6, 69.9, 69.6, 69.0, 69.0, 69.0, 70.5, 70.0, 68.8, 69.2, 69.2, 68.5, 68.5, 69.5, 70.1, 69.5, 69.0, 69.5, 68.9, 68.9, 70.1, 70.1, 69.6, 69.6, 69.0, 69.0, 68.0, 69.7, 69.7, 69.7, 69.7, 69.0, 69.0, 69.2, 70.2, 69.8, 69.8, 69.1, 69.1, 69.7, 69.2, 70.0, 70.0, 69.5, 69.5, 69.0, 69.0, 68.6, 69.9, 70.0, 70.0, 69.4, 69.4, 69.4, 68.8, 69.2, 69.9, 69.2, 69.1, 69.1, 68.6, 70.1, 70.4, 70.4, 69.3, 68.6, 69.1, 69.8, 70.1, 70.2, 70.2, 69.4, 69.4, 70.1, 70.1, 70.3, 70.6, 69.8, 69.6, 69.5, 69.4, 69.3, 68.9, 70.1, 70.1, 70.3, 69.5, 69.8, 69.5, 70.0, 70.4, 69.9, 70.1, 69.6, 69.0, 69.4, 70.0, 70.5, 70.5, 70.3, 70.4, 70.4, 69.8, 69.8, 70.4, 70.6, 71.1, 70.4, 70.0, 70.4, 71.0, 71.0, 70.4, 70.4, 69.8, 69.4, 70.5, 70.5, 70.4, 70.1, 71.0, 70.5, 70.3, 70.3, 70.3, 70.3, 71.7, 71.3, 70.7, 70.7, 70.9, 70.9, 70.9, 70.9, 70.9, 69.6, 69.6, 70.4, 71.3, 71.3, 71.3, 71.3, 71.3, 71.3, 71.8, 71.1, 71.3, 71.7, 71.3, 70.5, 70.6, 70.6, 70.6, 71.6, 71.1, 71.2, 71.2, 71.2, 72.0, 72.2, 70.7, 72.4, 71.7, 71.2, 71.2, 71.2, 71.2, 70.4, 69.8, 70.3, 69.7, 69.7, 69.7, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 71.1, 70.4, 70.4, 71.0, 70.4, 71.1, 71.1, 71.1, 71.1, 70.0, 69.1, 70.8, 70.0, 70.4, 70.0, 70.4, 70.4, 70.4, 70.4, 70.5, 70.4, 70.4, 70.4, 70.4, 71.0, 71.0, 71.0, 71.0, 70.9]

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