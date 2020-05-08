# Function Exercises Python for Everyone

grade = input("Tell the grade (scale from 0.0 to 1.0): ")
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

print(final_grade)