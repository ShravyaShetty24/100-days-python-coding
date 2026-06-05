# Course Registration System

students = []


# Register Student
def register_student():

    usn = input("Enter USN: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course Name: ")

    for s in students:
        if s["usn"] == usn:
            print("USN already registered")
            return

    student = {
        "usn": usn,
        "name": name,
        "course": course
    }

    students.append(student)

    print("Registration successful")


# View Registrations
def view_students():

    if len(students) == 0:
        print("No registrations found")

    else:

        print("\n------ REGISTRATIONS ------")

        for s in students:

            print("USN :", s["usn"])
            print("Name :", s["name"])
            print("Course :", s["course"])
            print()


# Search Student
def search_student():

    usn = input("Enter USN: ")

    for s in students:

        if s["usn"] == usn:

            print("\nStudent Found")
            print("Name :", s["name"])
            print("Course :", s["course"])

            return

    print("Student not found")


# Update Course
def update_course():

    usn = input("Enter USN: ")

    for s in students:

        if s["usn"] == usn:

            new_course = input("Enter New Course: ")

            s["course"] = new_course

            print("Course updated successfully")

            return

    print("Student not found")


# Cancel Registration
def cancel_registration():

    usn = input("Enter USN: ")

    for s in students:

        if s["usn"] == usn:

            students.remove(s)

            print("Registration cancelled")

            return

    print("Student not found")


# Main Program
while True:

    print("\n------ COURSE MENU ------")
    print("1. Register Student")
    print("2. View Registrations")
    print("3. Search Student")
    print("4. Update Course")
    print("5. Cancel Registration")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        register_student()

    elif ch == 2:
        view_students()

    elif ch == 3:
        search_student()

    elif ch == 4:
        update_course()

    elif ch == 5:
        cancel_registration()

    elif ch == 6:
        print("Thank You")
        break

    else:
        print("Invalid Choice")