#Append Marks
name=input("Enter student name:")
marks=input("Enter marks:")
file=open("marks.tex","a")
file.write(name + "-" + marks + "\n")
file.close()
print("Data appended successfully.")