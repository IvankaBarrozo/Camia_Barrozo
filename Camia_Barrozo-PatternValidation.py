import re

Student_id = input("Enter Student ID:")

Pattern= r"\d{4}-\d{4}"

if re.fullmatch(Pattern, Student_id):
    print("Valid Student ID.")

else:
    print("Invalid Student ID.")