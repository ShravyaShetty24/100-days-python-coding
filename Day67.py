# Student Attendance Management System

students = []

# Add Student
def add_student():

    student_id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    course = input("Enter Course: ")

    for s in students:
        if s["id"] == student_id:
            print("Student ID already exists")
            return

    student = {
        "id": student_id,
        "name": name,
        "course": course,
        "present": 0,
        "absent": 0
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
            print("ID :", s["id"])
            print("Name :", s["name"])
            print("Course :", s["course"])
            print("Present :", s["present"])
            print("Absent :", s["absent"])
            print()


# Mark Attendance
def mark_attendance():

    student_id = int(input("Enter Student ID: "))

    for s in students:

        if s["id"] == student_id:

            status = input("Present or Absent (P/A): ")

            if status.upper() == "P":
                s["present"] += 1
                print("Attendance marked as Present")

            elif status.upper() == "A":
                s["absent"] += 1
                print("Attendance marked as Absent")

            else:
                print("Invalid choice")

            return

    print("Student not found")


# Search Student
def search_student():

    student_id = int(input("Enter Student ID: "))

    for s in students:

        if s["id"] == student_id:

            print("\nStudent Found")
            print("Name :", s["name"])
            print("Course :", s["course"])
            print("Present :", s["present"])
            print("Absent :", s["absent"])
            return

    print("Student not found")


# Attendance Report
def attendance_report():

    for s in students:

        total = s["present"] + s["absent"]

        if total > 0:
            percentage = (s["present"] / total) * 100
        else:
            percentage = 0

        print("\nStudent :", s["name"])
        print("Attendance Percentage :", percentage, "%")


# Remove Student
def remove_student():

    student_id = int(input("Enter Student ID: "))

    for s in students:

        if s["id"] == student_id:

            students.remove(s)
            print("Student removed successfully")
            return

    print("Student not found")


# Main Program
while True:

    print("\n------ ATTENDANCE MENU ------")
    print("1. Add Student")
    print("2. View Students")
    print("3. Mark Attendance")
    print("4. Search Student")
    print("5. Attendance Report")
    print("6. Remove Student")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_student()

    elif ch == 2:
        view_students()

    elif ch == 3:
        mark_attendance()

    elif ch == 4:
        search_student()

    elif ch == 5:
        attendance_report()

    elif ch == 6:
        remove_student()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")