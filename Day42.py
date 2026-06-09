# Employee Attendance Management System

employees = []


# Add Employee
def add_employee():

    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")

    for e in employees:
        if e["id"] == emp_id:
            print("Employee ID already exists")
            return

    employee = {
        "id": emp_id,
        "name": name,
        "attendance": 0
    }

    employees.append(employee)

    print("Employee added successfully")


# Mark Attendance
def mark_attendance():

    emp_id = int(input("Enter Employee ID: "))

    for e in employees:

        if e["id"] == emp_id:

            e["attendance"] += 1

            print("Attendance marked successfully")

            return

    print("Employee not found")


# View Employees
def view_employees():

    if len(employees) == 0:
        print("No employees found")

    else:

        print("\n------ EMPLOYEE LIST ------")

        for e in employees:

            print("ID :", e["id"])
            print("Name :", e["name"])
            print("Attendance :", e["attendance"])
            print()


# Search Employee
def search_employee():

    emp_id = int(input("Enter Employee ID: "))

    for e in employees:

        if e["id"] == emp_id:

            print("\nEmployee Found")
            print("Name :", e["name"])
            print("Attendance :", e["attendance"])

            return

    print("Employee not found")


# Attendance Report
def attendance_report():

    if len(employees) == 0:
        print("No employee records found")

    else:

        highest = employees[0]

        for e in employees:

            if e["attendance"] > highest["attendance"]:
                highest = e

        print("\n------ ATTENDANCE REPORT ------")
        print("Employee :", highest["name"])
        print("Attendance :", highest["attendance"])


# Main Program
while True:

    print("\n------ ATTENDANCE MENU ------")
    print("1. Add Employee")
    print("2. Mark Attendance")
    print("3. View Employees")
    print("4. Search Employee")
    print("5. Attendance Report")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_employee()

    elif ch == 2:
        mark_attendance()

    elif ch == 3:
        view_employees()

    elif ch == 4:
        search_employee()

    elif ch == 5:
        attendance_report()

    elif ch == 6:
        print("Thank You")
        break

    else:
        print("Invalid Choice")