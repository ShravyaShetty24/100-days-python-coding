# Gym Membership Management System

members = []

# Add Member
def add_member():

    member_id = int(input("Enter Member ID: "))
    name = input("Enter Member Name: ")
    age = int(input("Enter Age: "))
    plan = input("Enter Plan (Basic/Silver/Gold): ")

    for m in members:
        if m["id"] == member_id:
            print("Member ID already exists")
            return

    if plan.lower() == "basic":
        fee = 2000
    elif plan.lower() == "silver":
        fee = 3500
    elif plan.lower() == "gold":
        fee = 5000
    else:
        print("Invalid Plan")
        return

    member = {
        "id": member_id,
        "name": name,
        "age": age,
        "plan": plan,
        "fee": fee,
        "status": "Active"
    }

    members.append(member)
    print("Member added successfully")


# View Members
def view_members():

    if len(members) == 0:
        print("No members found")
    else:
        print("\n------ MEMBER LIST ------")

        for m in members:
            print("ID :", m["id"])
            print("Name :", m["name"])
            print("Age :", m["age"])
            print("Plan :", m["plan"])
            print("Fee :", m["fee"])
            print("Status :", m["status"])
            print()


# Search Member
def search_member():

    member_id = int(input("Enter Member ID: "))

    for m in members:
        if m["id"] == member_id:
            print("\nMember Found")
            print("Name :", m["name"])
            print("Plan :", m["plan"])
            print("Fee :", m["fee"])
            print("Status :", m["status"])
            return

    print("Member not found")


# Renew Membership
def renew_membership():

    member_id = int(input("Enter Member ID: "))

    for m in members:
        if m["id"] == member_id:
            m["status"] = "Active"
            print("Membership renewed successfully")
            return

    print("Member not found")


# Remove Member
def remove_member():

    member_id = int(input("Enter Member ID: "))

    for m in members:
        if m["id"] == member_id:
            members.remove(m)
            print("Member removed successfully")
            return

    print("Member not found")


# Membership Report
def membership_report():

    active = 0

    for m in members:
        if m["status"] == "Active":
            active += 1

    print("Total Members =", len(members))
    print("Active Members =", active)


# Main Program
while True:

    print("\n------ GYM MEMBERSHIP MENU ------")
    print("1. Add Member")
    print("2. View Members")
    print("3. Search Member")
    print("4. Renew Membership")
    print("5. Remove Member")
    print("6. Membership Report")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_member()

    elif ch == 2:
        view_members()

    elif ch == 3:
        search_member()

    elif ch == 4:
        renew_membership()

    elif ch == 5:
        remove_member()

    elif ch == 6:
        membership_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")