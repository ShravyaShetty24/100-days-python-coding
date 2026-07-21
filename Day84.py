#safe divider

try:
   a=int(input("Enter the value of a:"))
   b=int(input("Enter the value of b:"))
   print(a/b)
except ZeroDivisionError:
   print("division by zero is not allowed")
except ValueError:
   print("please enter valid input")
print()


#file reader

try:
   filename=input("Enter file name:")
   file=open(filename,"c")
   print(file.read)
   file.close()
except FileNotFoundError:
   print("file does not exist")
finally:
   print("program found")