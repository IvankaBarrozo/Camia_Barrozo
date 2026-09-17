import re

try:
    Examination_score = int(input("Enter Examination Score: "))

    if 0<= Examination_score <= 100:
        print("Valid score.")

    else:
        print("Invalid score.")

except ValueError:
    print("Invalid input. Please enter a number.")