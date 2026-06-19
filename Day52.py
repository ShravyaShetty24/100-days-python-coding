# Student Result Management System

students = []

# Add Student Result
def add_student():

    usn = input("Enter USN: ")
    name = input("Enter Student Name: ")
    marks = int(input("Enter Total Marks (Out of 500): "))

    percentage = (marks / 500) * 100

    if percentage >= 35:
        result = "Pass"
    else:
        result = "Fail"

    student = {
        "usn": usn,
        "name": name,
        "marks": marks,
        "percentage": percentage,
        "result": result
    }

    students.append(student)

    print("Student result added successfully")


# View Results
def view_results():

    if len(students) == 0:
        print("No records found")

    else:

        print("\n------ RESULT LIST ------")

        for s in students:

            print("USN :", s["usn"])
            print("Name :", s["name"])
            print("Marks :", s["marks"])
            print("Percentage :", s["percentage"])
            print("Result :", s["result"])
            print()


# Search Student
def search_student():

    usn = input("Enter USN: ")

    for s in students:

        if s["usn"] == usn:

            print("\nStudent Found")
            print("Name :", s["name"])
            print("Marks :", s["marks"])
            print("Percentage :", s["percentage"])
            print("Result :", s["result"])

            return

    print("Student not found")


# Update Marks
def update_marks():

    usn = input("Enter USN: ")

    for s in students:

        if s["usn"] == usn:

            marks = int(input("Enter New Marks: "))

            percentage = (marks / 500) * 100

            if percentage >= 35:
                result = "Pass"
            else:
                result = "Fail"

            s["marks"] = marks
            s["percentage"] = percentage
            s["result"] = result

            print("Marks updated successfully")

            return

    print("Student not found")


# Delete Student
def delete_student():

    usn = input("Enter USN: ")

    for s in students:

        if s["usn"] == usn:

            students.remove(s)

            print("Student record deleted")

            return

    print("Student not found")


# Result Report
def result_report():

    pass_count = 0
    fail_count = 0

    for s in students:

        if s["result"] == "Pass":
            pass_count += 1
        else:
            fail_count += 1

    print("Pass Students =", pass_count)
    print("Fail Students =", fail_count)


# Main Program
while True:

    print("\n------ RESULT MENU ------")
    print("1. Add Student Result")
    print("2. View Results")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Result Report")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_student()

    elif ch == 2:
        view_results()

    elif ch == 3:
        search_student()

    elif ch == 4:
        update_marks()

    elif ch == 5:
        delete_student()

    elif ch == 6:
        result_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")