# Hospital Patient Management System

patients = []


# Add Patient
def add_patient():

    patient_id = int(input("Enter Patient ID: "))
    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))
    disease = input("Enter Disease: ")

    for p in patients:
        if p["id"] == patient_id:
            print("Patient ID already exists")
            return

    patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "disease": disease
    }

    patients.append(patient)

    print("Patient added successfully")


# View Patients
def view_patients():

    if len(patients) == 0:
        print("No patient records found")

    else:

        print("\n------ PATIENT LIST ------")

        for p in patients:

            print("ID :", p["id"])
            print("Name :", p["name"])
            print("Age :", p["age"])
            print("Disease :", p["disease"])
            print()


# Search Patient
def search_patient():

    patient_id = int(input("Enter Patient ID: "))

    for p in patients:

        if p["id"] == patient_id:

            print("\nPatient Found")
            print("Name :", p["name"])
            print("Age :", p["age"])
            print("Disease :", p["disease"])

            return

    print("Patient not found")


# Update Disease
def update_disease():

    patient_id = int(input("Enter Patient ID: "))

    for p in patients:

        if p["id"] == patient_id:

            new_disease = input("Enter New Disease: ")

            p["disease"] = new_disease

            print("Disease updated successfully")

            return

    print("Patient not found")


# Discharge Patient
def discharge_patient():

    patient_id = int(input("Enter Patient ID: "))

    for p in patients:

        if p["id"] == patient_id:

            patients.remove(p)

            print("Patient discharged successfully")

            return

    print("Patient not found")


# Patient Report
def patient_report():

    print("Total Patients =", len(patients))


# Main Program
while True:

    print("\n------ HOSPITAL MENU ------")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Update Disease")
    print("5. Discharge Patient")
    print("6. Patient Report")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_patient()

    elif ch == 2:
        view_patients()

    elif ch == 3:
        search_patient()

    elif ch == 4:
        update_disease()

    elif ch == 5:
        discharge_patient()

    elif ch == 6:
        patient_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")