#Search from file

search_name=input("Enter name to search:")
file=open("friends.tex","r")
found=False
for line in file:
    if line.strip()==search_name:
        found=True
        break
file.close
if found:
    print("found!")
else:
    print("Not found!")