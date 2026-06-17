# Student Placement Management System

students = []


# Add Student
def add_student():

    usn = input("Enter USN: ")
    name = input("Enter Name: ")
    company = input("Enter Company Name: ")
    package = float(input("Enter Package (LPA): "))

    student = {
        "usn": usn,
        "name": name,
        "company": company,
        "package": package,
        "placed": True
    }

    students.append(student)

    print("Student added successfully")


# View Students
def view_students():

    if len(students) == 0:
        print("No student records found")

    else:

        print("\n------ STUDENT LIST ------")

        for s in students:

            print("USN :", s["usn"])
            print("Name :", s["name"])
            print("Company :", s["company"])
            print("Package :", s["package"], "LPA")
            print("Placed :", s["placed"])
            print()


# Search Student
def search_student():

    usn = input("Enter USN: ")

    for s in students:

        if s["usn"] == usn:

            print("\nStudent Found")
            print("Name :", s["name"])
            print("Company :", s["company"])
            print("Package :", s["package"])

            return

    print("Student not found")


# Update Placement
def update_placement():

    usn = input("Enter USN: ")

    for s in students:

        if s["usn"] == usn:

            company = input("Enter New Company: ")
            package = float(input("Enter New Package: "))

            s["company"] = company
            s["package"] = package

            print("Placement updated successfully")

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


# Placement Report
def placement_report():

    count = 0

    for s in students:

        if s["placed"] == True:
            count += 1

    print("Total Placed Students =", count)


# Main Program
while True:

    print("\n------ PLACEMENT MENU ------")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Placement")
    print("5. Delete Student")
    print("6. Placement Report")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_student()

    elif ch == 2:
        view_students()

    elif ch == 3:
        search_student()

    elif ch == 4:
        update_placement()

    elif ch == 5:
        delete_student()

    elif ch == 6:
        placement_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")