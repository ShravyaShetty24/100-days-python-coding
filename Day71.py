# Blood Bank Management System

donors = []

# Add Donor
def add_donor():

    donor_id = int(input("Enter Donor ID: "))
    name = input("Enter Donor Name: ")
    age = int(input("Enter Age: "))
    blood_group = input("Enter Blood Group: ")

    for d in donors:
        if d["id"] == donor_id:
            print("Donor ID already exists")
            return

    donor = {
        "id": donor_id,
        "name": name,
        "age": age,
        "blood_group": blood_group,
        "donations": 0
    }

    donors.append(donor)
    print("Donor added successfully")


# View Donors
def view_donors():

    if len(donors) == 0:
        print("No donor records found")
    else:
        print("\n------ DONOR LIST ------")

        for d in donors:
            print("ID :", d["id"])
            print("Name :", d["name"])
            print("Age :", d["age"])
            print("Blood Group :", d["blood_group"])
            print("Total Donations :", d["donations"])
            print()


# Search Donor
def search_donor():

    donor_id = int(input("Enter Donor ID: "))

    for d in donors:

        if d["id"] == donor_id:

            print("\nDonor Found")
            print("Name :", d["name"])
            print("Blood Group :", d["blood_group"])
            print("Donations :", d["donations"])
            return

    print("Donor not found")


# Donate Blood
def donate_blood():

    donor_id = int(input("Enter Donor ID: "))

    for d in donors:

        if d["id"] == donor_id:

            d["donations"] += 1
            print("Blood donation recorded successfully")
            return

    print("Donor not found")


# Update Blood Group
def update_blood_group():

    donor_id = int(input("Enter Donor ID: "))

    for d in donors:

        if d["id"] == donor_id:

            new_group = input("Enter New Blood Group: ")
            d["blood_group"] = new_group

            print("Blood group updated successfully")
            return

    print("Donor not found")


# Blood Bank Report
def blood_bank_report():

    total_donations = 0

    for d in donors:
        total_donations += d["donations"]

    print("Total Donors =", len(donors))
    print("Total Blood Donations =", total_donations)


# Main Program
while True:

    print("\n------ BLOOD BANK MENU ------")
    print("1. Add Donor")
    print("2. View Donors")
    print("3. Search Donor")
    print("4. Donate Blood")
    print("5. Update Blood Group")
    print("6. Blood Bank Report")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_donor()

    elif ch == 2:
        view_donors()

    elif ch == 3:
        search_donor()

    elif ch == 4:
        donate_blood()

    elif ch == 5:
        update_blood_group()

    elif ch == 6:
        blood_bank_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")