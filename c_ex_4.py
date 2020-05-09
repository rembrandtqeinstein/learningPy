# Function Exercises Python for Everyone
hours = input("How many hours you work: ")
rate = input("How many you are payed per hour: ")

def computePay(hours, rate):
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
    return pay

print(computePay(hours,rate))

grade = input("Tell the grade (scale from 0.0 to 1.0): ")

def computeGrade(grade):
    try:
        grade = float(grade)
    except:
        print("Bad score")
        quit()

    if grade > 1.0:
        final_grade = 'Bad Score'
    elif grade >= 0.9:
        final_grade = 'A'
    elif grade >= 0.8:
        final_grade = 'B'
    elif grade >= 0.7:
        final_grade = 'C'
    elif grade >= 0.6:
        final_grade = 'D'
    elif grade >= 0:
        final_grade = 'F'
    else:
        final_grade = 'Bad Score'
    return final_grade

print(computeGrade(grade))