#building a calculator
num1=float(input("Enetr the no.1: "))
num2=float(input("Enter the no.2: "))
op=input("Enter the operator")
if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    if num2==0:
       print("Error:Division by zero is not allowed")
    else:
        print(num1/num2)
elif op=="%":
    if num2==0:
       print("Error:Division by zero is not allowed")
    else:
        print(num1/num2)
else:
   print("Invalid operator:")   