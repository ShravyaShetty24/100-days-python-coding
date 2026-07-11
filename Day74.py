# Employee Leave Management System

employees = []

# Add Employee
def add_employee():

    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")

    for e in employees:
        if e["id"] == emp_id:
            print("Employee ID already exists")
            return

    employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "leave_days": 0,
        "status": "No Leave"
    }

    employees.append(employee)
    print("Employee added successfully")


# View Employees
def view_employees():

    if len(employees) == 0:
        print("No employee records found")

    else:
        print("\n------ EMPLOYEE LIST ------")

        for e in employees:
            print("ID :", e["id"])
            print("Name :", e["name"])
            print("Department :", e["department"])
            print("Leave Days :", e["leave_days"])
            print("Status :", e["status"])
            print()


# Search Employee
def search_employee():

    emp_id = int(input("Enter Employee ID: "))

    for e in employees:

        if e["id"] == emp_id:

            print("\nEmployee Found")
            print("Name :", e["name"])
            print("Department :", e["department"])
            print("Leave Days :", e["leave_days"])
            print("Status :", e["status"])
            return

    print("Employee not found")


# Apply Leave
def apply_leave():

    emp_id = int(input("Enter Employee ID: "))

    for e in employees:

        if e["id"] == emp_id:

            days = int(input("Enter Number of Leave Days: "))
            e["leave_days"] = days
            e["status"] = "Pending"

            print("Leave applied successfully")
            return

    print("Employee not found")


# Approve Leave
def approve_leave():

    emp_id = int(input("Enter Employee ID: "))

    for e in employees:

        if e["id"] == emp_id:

            if e["leave_days"] > 0:
                e["status"] = "Approved"
                print("Leave approved successfully")
            else:
                print("No leave application found")

            return

    print("Employee not found")


# Leave Report
def leave_report():

    approved = 0

    for e in employees:
        if e["status"] == "Approved":
            approved += 1

    print("Total Employees =", len(employees))
    print("Approved Leaves =", approved)
    print("Pending Leaves =", len(employees) - approved)


# Main Program
while True:

    print("\n------ LEAVE MANAGEMENT MENU ------")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Apply Leave")
    print("5. Approve Leave")
    print("6. Leave Report")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_employee()

    elif ch == 2:
        view_employees()

    elif ch == 3:
        search_employee()

    elif ch == 4:
        apply_leave()

    elif ch == 5:
        approve_leave()

    elif ch == 6:
        leave_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")