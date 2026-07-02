# Employee Payroll Management System

employees = []


# Add Employee
def add_employee():

    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    designation = input("Enter Designation: ")
    basic_salary = float(input("Enter Basic Salary: "))

    for e in employees:
        if e["id"] == emp_id:
            print("Employee ID already exists")
            return

    hra = basic_salary * 0.20
    da = basic_salary * 0.10
    net_salary = basic_salary + hra + da

    employee = {
        "id": emp_id,
        "name": name,
        "designation": designation,
        "basic_salary": basic_salary,
        "net_salary": net_salary
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
            print("Designation :", e["designation"])
            print("Basic Salary :", e["basic_salary"])
            print("Net Salary :", e["net_salary"])
            print()


# Search Employee
def search_employee():

    emp_id = int(input("Enter Employee ID: "))

    for e in employees:

        if e["id"] == emp_id:

            print("\nEmployee Found")
            print("Name :", e["name"])
            print("Designation :", e["designation"])
            print("Net Salary :", e["net_salary"])
            return

    print("Employee not found")


# Update Salary
def update_salary():

    emp_id = int(input("Enter Employee ID: "))

    for e in employees:

        if e["id"] == emp_id:

            basic_salary = float(input("Enter New Basic Salary: "))

            hra = basic_salary * 0.20
            da = basic_salary * 0.10
            net_salary = basic_salary + hra + da

            e["basic_salary"] = basic_salary
            e["net_salary"] = net_salary

            print("Salary updated successfully")
            return

    print("Employee not found")


# Generate Salary Slip
def salary_slip():

    emp_id = int(input("Enter Employee ID: "))

    for e in employees:

        if e["id"] == emp_id:

            print("\n------ SALARY SLIP ------")
            print("Employee ID :", e["id"])
            print("Name :", e["name"])
            print("Designation :", e["designation"])
            print("Basic Salary :", e["basic_salary"])
            print("HRA :", e["basic_salary"] * 0.20)
            print("DA :", e["basic_salary"] * 0.10)
            print("Net Salary :", e["net_salary"])

            return

    print("Employee not found")


# Payroll Report
def payroll_report():

    total_salary = 0

    for e in employees:
        total_salary += e["net_salary"]

    print("Total Payroll Amount =", total_salary)


# Main Program
while True:

    print("\n------ PAYROLL MENU ------")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Generate Salary Slip")
    print("6. Payroll Report")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_employee()

    elif ch == 2:
        view_employees()

    elif ch == 3:
        search_employee()

    elif ch == 4:
        update_salary()

    elif ch == 5:
        salary_slip()

    elif ch == 6:
        payroll_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")