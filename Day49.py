class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    def display(self):
        print(f"Doctor ID: {self.doctor_id}")
        print(f"Name: {self.name}")
        print(f"Specialization: {self.specialization}")


class Patient:
    def __init__(self, patient_id, name, disease):
        self.patient_id = patient_id
        self.name = name
        self.disease = disease

    def display(self):
        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Disease: {self.disease}")


class Appointment:
    def __init__(self, doctor, patient, date):
        self.doctor = doctor
        self.patient = patient
        self.date = date

    def display(self):
        print("\nAppointment Details")
        print(f"Date: {self.date}")
        print(f"Doctor: {self.doctor.name}")
        print(f"Patient: {self.patient.name}")


# Driver Program
d1 = Doctor(101, "Ravi", "Cardiologist")
p1 = Patient(201, "Shravya", "Heart Problem")

app = Appointment(d1, p1, "15-06-2026")

print("Doctor Details:")
d1.display()

print("\nPatient Details:")
p1.display()

app.display()