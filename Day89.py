#create a file and write

file=open("friends.tex","w")
for i in range(3):
    name=input("Enter friend name: ")
    file.write(name+"\n")
file.close()
print("name saved successfully.")