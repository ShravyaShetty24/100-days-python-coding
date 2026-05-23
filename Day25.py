# Student Result Management System

students = []

def add_student():

    name = input("Enter student name: ")

    m1 = int(input("Enter marks of Subject 1: "))
    m2 = int(input("Enter marks of Subject 2: "))
    m3 = int(input("Enter marks of Subject 3: "))

    marks = [m1, m2, m3]

    total = sum(marks)

    average = total / len(marks)

    # Grade Calculation
    if average >= 90:
        grade = "A+"

    elif average >= 75:
        grade = "A"

    elif average >= 60:
        grade = "B"

    elif average >= 40:
        grade = "C"

    else:
        grade = "Fail"

    student = {
        "name": name,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    students.append(student)

    print("Student added successfully")

def view_results():

    if len(students) == 0:
        print("No student records found")

    else:

        print("\n------ STUDENT RESULTS ------")

        for s in students:

            print("Name :", s["name"])
            print("Marks :", s["marks"])
            print("Total :", s["total"])
            print("Average :", round(s["average"], 2))
            print("Grade :", s["grade"])
            print()

def search_student():

    name = input("Enter student name to search: ")

    for s in students:

        if s["name"].lower() == name.lower():

            print("\nStudent Found")
            print("Name :", s["name"])
            print("Marks :", s["marks"])
            print("Total :", s["total"])
            print("Average :", round(s["average"], 2))
            print("Grade :", s["grade"])

            return

    print("Student not found")

while True:

    print("\n------ RESULT MENU ------")
    print("1. Add Student")
    print("2. View Results")
    print("3. Search Student")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_student()

    elif ch == 2:
        view_results()

    elif ch == 3:
        search_student()

    elif ch == 4:
        print("Thank You")
        break

    else:
        print("Invalid Choice")