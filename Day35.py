# Hospital Appointment Management System

appointments = []


# Function to add appointment
def add_appointment():

    patient_id = int(input("Enter Patient ID: "))
    patient_name = input("Enter Patient Name: ")
    doctor = input("Enter Doctor Name: ")
    date = input("Enter Appointment Date (DD-MM-YYYY): ")
    time = input("Enter Appointment Time: ")

    # Check duplicate appointment
    for a in appointments:

        if (a["patient_id"] == patient_id and
                a["date"] == date and
                a["time"] == time):

            print("Appointment already exists")
            return

    appointment = {
        "patient_id": patient_id,
        "patient_name": patient_name,
        "doctor": doctor,
        "date": date,
        "time": time
    }

    appointments.append(appointment)

    print("Appointment added successfully")


# Function to view appointments
def view_appointments():

    if len(appointments) == 0:
        print("No appointments found")

    else:

        print("\n------ APPOINTMENTS ------")

        for a in appointments:

            print("Patient ID :", a["patient_id"])
            print("Patient Name :", a["patient_name"])
            print("Doctor :", a["doctor"])
            print("Date :", a["date"])
            print("Time :", a["time"])
            print()


# Function to search patient
def search_patient():

    patient_id = int(input("Enter Patient ID to search: "))

    for a in appointments:

        if a["patient_id"] == patient_id:

            print("\nPatient Found")
            print("Patient Name :", a["patient_name"])
            print("Doctor :", a["doctor"])
            print("Date :", a["date"])
            print("Time :", a["time"])

            return

    print("Patient not found")


# Function to cancel appointment
def cancel_appointment():

    patient_id = int(input("Enter Patient ID to cancel appointment: "))

    for a in appointments:

        if a["patient_id"] == patient_id:

            appointments.remove(a)

            print("Appointment cancelled successfully")

            return

    print("Appointment not found")


# Function to view doctor's schedule
def doctor_schedule():

    doctor = input("Enter Doctor Name: ")

    found = False

    print("\n------ DOCTOR SCHEDULE ------")

    for a in appointments:

        if a["doctor"].lower() == doctor.lower():

            print("Patient :", a["patient_name"])
            print("Date :", a["date"])
            print("Time :", a["time"])
            print()

            found = True

    if not found:
        print("No appointments found for this doctor")


# Main Program
while True:

    print("\n------ HOSPITAL MENU ------")
    print("1. Add Appointment")
    print("2. View Appointments")
    print("3. Search Patient")
    print("4. Cancel Appointment")
    print("5. Doctor Schedule")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_appointment()

    elif ch == 2:
        view_appointments()

    elif ch == 3:
        search_patient()

    elif ch == 4:
        cancel_appointment()

    elif ch == 5:
        doctor_schedule()

    elif ch == 6:
        print("Thank You")
        break

    else:
        print("Invalid Choice")