#import pandas as pd

hours = input("How many hours you work: ")
rate = input("How many you are payed per hour: ")
try:
    hrs = float(hours)
    fra = float(rate)
except:
    print("That is not a number")
    quit()

if hrs >= 40:
    pay = 40 * fra
    pay = pay + ((hrs - 40) * 1.5)
else:
    pay = hrs * fra
print(pay)
#print(pd.datetime)