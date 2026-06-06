# Gym Membership Management System

members = []


# Add Member
def add_member():

    member_id = int(input("Enter Member ID: "))
    name = input("Enter Member Name: ")
    plan = input("Enter Plan (Monthly/Quarterly/Yearly): ")

    for m in members:
        if m["id"] == member_id:
            print("Member ID already exists")
            return

    if plan.lower() == "monthly":
        fee = 1000

    elif plan.lower() == "quarterly":
        fee = 2500

    elif plan.lower() == "yearly":
        fee = 9000

    else:
        print("Invalid Plan")
        return

    member = {
        "id": member_id,
        "name": name,
        "plan": plan,
        "fee": fee
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
            print("Plan :", m["plan"])
            print("Fee :", m["fee"])
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

            return

    print("Member not found")


# Update Plan
def update_plan():

    member_id = int(input("Enter Member ID: "))

    for m in members:

        if m["id"] == member_id:

            new_plan = input("Enter New Plan: ")

            if new_plan.lower() == "monthly":
                m["fee"] = 1000

            elif new_plan.lower() == "quarterly":
                m["fee"] = 2500

            elif new_plan.lower() == "yearly":
                m["fee"] = 9000

            else:
                print("Invalid Plan")
                return

            m["plan"] = new_plan

            print("Plan updated successfully")

            return

    print("Member not found")


# Delete Member
def delete_member():

    member_id = int(input("Enter Member ID: "))

    for m in members:

        if m["id"] == member_id:

            members.remove(m)

            print("Member deleted successfully")

            return

    print("Member not found")


# Total Fee Collection
def total_fee():

    total = 0

    for m in members:
        total += m["fee"]

    print("Total Fee Collection =", total)


# Main Program
while True:

    print("\n------ GYM MENU ------")
    print("1. Add Member")
    print("2. View Members")
    print("3. Search Member")
    print("4. Update Plan")
    print("5. Delete Member")
    print("6. Total Fee Collection")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_member()

    elif ch == 2:
        view_members()

    elif ch == 3:
        search_member()

    elif ch == 4:
        update_plan()

    elif ch == 5:
        delete_member()

    elif ch == 6:
        total_fee()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")