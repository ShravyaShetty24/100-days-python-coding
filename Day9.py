#student marks manager
marks=[98,56,88,45,76]
print("marks:",marks)
print("Hieghest marks: ",max(marks))
print("Lowest marks: ",min(marks))
avg=sum(marks)/len(marks)
print("Average: ",avg)
marks.append(36)
marks.remove(56)
print("Updated marks: ",marks)