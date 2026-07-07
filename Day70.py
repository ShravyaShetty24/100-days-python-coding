# Hostel Room Allocation Management System

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
        "room_no": None,
        "status": "Not Allocated"
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
            print("Room No :", s["room_no"])
            print("Status :", s["status"])
            print()


# Search Student
def search_student():

    student_id = int(input("Enter Student ID: "))

    for s in students:
        if s["id"] == student_id:
            print("\nStudent Found")
            print("Name :", s["name"])
            print("Course :", s["course"])
            print("Room No :", s["room_no"])
            print("Status :", s["status"])
            return

    print("Student not found")


# Allocate Room
def allocate_room():

    student_id = int(input("Enter Student ID: "))

    for s in students:
        if s["id"] == student_id:

            if s["status"] == "Allocated":
                print("Room already allocated")
                return

            room = int(input("Enter Room Number: "))
            s["room_no"] = room
            s["status"] = "Allocated"

            print("Room allocated successfully")
            return

    print("Student not found")


# Vacate Room
def vacate_room():

    student_id = int(input("Enter Student ID: "))

    for s in students:
        if s["id"] == student_id:

            if s["status"] == "Not Allocated":
                print("No room allocated")
                return

            s["room_no"] = None
            s["status"] = "Not Allocated"

            print("Room vacated successfully")
            return

    print("Student not found")


# Hostel Report
def hostel_report():

    allocated = 0

    for s in students:
        if s["status"] == "Allocated":
            allocated += 1

    print("Total Students =", len(students))
    print("Rooms Allocated =", allocated)
    print("Rooms Vacant =", len(students) - allocated)


# Main Program
while True:

    print("\n------ HOSTEL MENU ------")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Allocate Room")
    print("5. Vacate Room")
    print("6. Hostel Report")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_student()

    elif ch == 2:
        view_students()

    elif ch == 3:
        search_student()

    elif ch == 4:
        allocate_room()

    elif ch == 5:
        vacate_room()

    elif ch == 6:
        hostel_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")