#implementing online shopping cart system
cart=[]
def add_product():
    name=input("enter product name:")
    price=float(input("Enter product price:"))
    quantity=int(input("Enter product quantity"))
    product={
        "name":name,
        "price":price,
        "qty":quantity
    }
    cart.append(product)
    print("Product added successfully")

def view_cart():
    if len(cart)==0:
        print("cart if empty")
    else:
        print("\n----CART ITEMs----")
        for item in cart:
            print("Product: ",item["name"])
            print("price: ",item["price"])
            print("quantity: ",item["qty"])
            print()

def remove_product():
    name=input("Enter the product name to remove:")
    for item in cart:
        if item["name"].lower()==name.lower():
            cart.remove(item)
            print("Product removed successfully")
            return
    print("Product not found")

def total_bill():
    total=0
    for item in cart:
        total+=item["price"]*item["qty"]
    print("\nTotal bill=",total)
    discount=lambda x: x*0.10
    if total>5000:
        discount_amont=discount(total)
        final_amount=total-discount_amont
        print("Discount=",discount_amont)
        print("Final Amount=",final_amount)
    else:
        print("No discount appllied")
while True:
    print("\n----SHOPPING MENU-----")
    print("1. Add Product")
    print("2. View Cart")
    print("3. Remove Product")
    print("4. Total Bill")
    print("5. Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        add_product()
    elif ch==2:
        view_cart()
    elif ch==3:
        remove_product()
    elif ch==4:
        total_bill()
    elif ch==5:
        print("Thank You for Shopping")
        break
    else:
        print("Invalid Choice")