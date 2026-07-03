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
        "disease": disease,
        "admitted": True
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

            status = "Admitted" if p["admitted"] else "Discharged"

            print("ID :", p["id"])
            print("Name :", p["name"])
            print("Age :", p["age"])
            print("Disease :", p["disease"])
            print("Status :", status)
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
            print("Status :", "Admitted" if p["admitted"] else "Discharged")
            return

    print("Patient not found")


# Update Diagnosis
def update_diagnosis():

    patient_id = int(input("Enter Patient ID: "))

    for p in patients:

        if p["id"] == patient_id:

            new_disease = input("Enter New Diagnosis: ")
            p["disease"] = new_disease

            print("Diagnosis updated successfully")
            return

    print("Patient not found")


# Discharge Patient
def discharge_patient():

    patient_id = int(input("Enter Patient ID: "))

    for p in patients:

        if p["id"] == patient_id:

            if p["admitted"]:
                p["admitted"] = False
                print("Patient discharged successfully")
            else:
                print("Patient is already discharged")

            return

    print("Patient not found")


# Hospital Report
def hospital_report():

    admitted = 0
    discharged = 0

    for p in patients:

        if p["admitted"]:
            admitted += 1
        else:
            discharged += 1

    print("Total Patients =", len(patients))
    print("Admitted Patients =", admitted)
    print("Discharged Patients =", discharged)


# Main Program
while True:

    print("\n------ HOSPITAL MENU ------")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Update Diagnosis")
    print("5. Discharge Patient")
    print("6. Hospital Report")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_patient()

    elif ch == 2:
        view_patients()

    elif ch == 3:
        search_patient()

    elif ch == 4:
        update_diagnosis()

    elif ch == 5:
        discharge_patient()

    elif ch == 6:
        hospital_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")