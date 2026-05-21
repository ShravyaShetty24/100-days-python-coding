#online shopping cart system
#cart=[]
while True:
    print("\n1.Add Product")
    print("\n2.View Cart")
    print("\n3.Exit")
    choice=int(input("Enter choice:"))
    if choice==1:
        print("Add product selected")
    elif choice==2:
        print("View Cart selected")
    elif choice==3:
        break
    else:
        print("invalid choice")