#improved version
# Student Health Report Analyzer

def check_hemoglobin(hb):
    if hb < 12:
        return "Low"
    elif hb <= 16:
        return "Normal"
    else:
        return "High"


def check_sugar(sugar):
    if sugar < 70:
        return "Low"
    elif sugar <= 140:
        return "Normal"
    else:
        return "High"


def check_cholesterol(chol):
    if chol < 200:
        return "Normal"
    else:
        return "High"


students = []
healthy_count = 0

n = int(input("Enter number of students: "))

for i in range(n):

    print("\nStudent", i + 1)

    name = input("Enter student name: ")
    hb = float(input("Enter hemoglobin level: "))
    sugar = float(input("Enter blood sugar level: "))
    chol = float(input("Enter cholesterol level: "))

    hb_status = check_hemoglobin(hb)
    sugar_status = check_sugar(sugar)
    chol_status = check_cholesterol(chol)

    student = {
        "Name": name,
        "Hemoglobin": hb_status,
        "Sugar": sugar_status,
        "Cholesterol": chol_status
    }

    students.append(student)

    if hb_status == "Normal" and sugar_status == "Normal" and chol_status == "Normal":
        healthy_count += 1

    print("\nHealth Report")
    print("-------------------")
    print("Hemoglobin :", hb_status)
    print("Blood Sugar :", sugar_status)
    print("Cholesterol :", chol_status)

    if healthy_count:
        print("Suggestion: Maintain healthy lifestyle.")
    else:
        print("Suggestion: Consult doctor and improve diet.")


print("\nAll Student Reports")
print("----------------------")

for s in students:
    print(s)

print("\nHealthy Students Count:", healthy_count)