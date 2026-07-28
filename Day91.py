#Read and Count Lines
file=open("marks.tex","r")
lines=file.readlines()
count=len(lines)
print("Number of students:",count)
file.close()