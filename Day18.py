#student Health Report analyzer
name=input("Enter student name:")

hemoglobin=float(input("Enter hemoglobin:"))
sugar=float(input("Enter sugar:"))
cholesterol=float(input("Enter cholesterol:"))

print("Health Report")
print("------------")

#hemoglobin check
if hemoglobin<12:
    print("Hemoglobin : Low")
elif hemoglobin>=12 and hemoglobin<=16:
    print("Hemoglobin : Normal")
else:
    print("Hemoglobin : High")
#sugar check
if sugar<70:
    print("Blood sugar : Low")
elif sugar>=70 and sugar<=140:
    print("Blood sugar : Normal")
else:
    print("Blood sugar : High")
#cholesterol check
if cholesterol<200:
    print("Cholesterol : Normal")
else:
    print("Cholesterol : High")

print("Suggestion:")
print("Take healthy diet and if needed consult a doctor.")