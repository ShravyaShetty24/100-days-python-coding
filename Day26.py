#Employee Payroll Management System
emp=[]
def emp_det():
    empid=int(input("Enter empolyee id:"))
    ename=input("Enter empolyee name:")
    salary=float(input("Enter empolyee salary:"))
    
    if salary>5000:
        bonus=salary*0.10
    elif 30000<salary<50000:
        bonus=salary*0.05
    else:
        bonus=0

    final_salary=salary+bonus

    employe={
        "id":empid,
        "name":ename,
        "salary":salary,
        "bonus":bonus,
        "final salary":final_salary
    } 
    emp.append(employe)
    print("employee deatils added successfully")

def veiw_empdet():
    if len(emp)==0:
        print("no employee record found")
    else:
        for e in emp:
            print("\n-----EMPLOYEE DETAILS-----")
            print("e_id:",e["id"])
            print("Name:",e["name"])
            print("basic salary:",e["salary"])
            print("bonus:",e["bonus"])
            print("final salary:",e["final salary"])
            print()

def emp_search():
    name=input("Enter emp name to search:")
    for e in emp:
        if e["name"].lower()==name.lower():
            print("\n employee found")
            print("e_id:",e["id"])
            print("Name:",e["name"])
            print("basic salary:",e["salary"])
            print("bonus:",e["bonus"])
            print("final salary:",e["final salary"])
            return
        else:
            print("no employee found")
while True:
    print("\n-----Result Menu----")
    print("1.Add employee details")
    print("2.View employee record")
    print("3.search emplyee")
    print("4.Exit")

    ch=int(input("Enter your choice:"))
    if ch==1:
        emp_det()
    elif ch==2:
        veiw_empdet()
    elif ch==3:
        emp_search()
    elif ch==4:
        print("Thank You")
        break
    else:
        print("invalid choice")