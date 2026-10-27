
name = input("Enter Student Name: ")
marks = float(input("Enter Marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks! Enter marks between 0 and 100.")
else:
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "Fail"

    print("\nStudent Name:", name)
    print("Marks:", marks)
    print("Grade:", grade)
