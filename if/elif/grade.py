score = int(input("Enter your test score (0-100):  "))

if score >= 90:
    grade = "A"
    print("Excellent Work! ")
elif score >= 80:
    grade = "B"
    print("Good Job")
elif score >= 70:
    grade = "C"
    print("keep trying")
elif score >= 60:
    grade = "D"
    print("You need to study more ")
else:
    grade = "F"
    print("Lets work on improving")

print(f"Your grade: {grade}")

# Note the F at line 19  inserts variables inside text 