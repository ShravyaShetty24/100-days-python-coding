# Supermarket Billing Management System

products = []
total_sales = 0

# Add Product
def add_product():

    product_id = int(input("Enter Product ID: "))
    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))
    stock = int(input("Enter Stock Quantity: "))

    for p in products:
        if p["id"] == product_id:
            print("Product ID already exists")
            return

    product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }

    products.append(product)

    print("Product added successfully")


# View Products
def view_products():

    if len(products) == 0:
        print("No products available")

    else:
        print("\n------ PRODUCT LIST ------")

        for p in products:
            print("ID :", p["id"])
            print("Name :", p["name"])
            print("Price :", p["price"])
            print("Stock :", p["stock"])
            print()


# Search Product
def search_product():

    product_id = int(input("Enter Product ID: "))

    for p in products:
        if p["id"] == product_id:
            print("Product Found")
            print("Name :", p["name"])
            print("Price :", p["price"])
            print("Stock :", p["stock"])
            return

    print("Product not found")


# Purchase Product
def purchase_product():

    global total_sales

    product_id = int(input("Enter Product ID: "))
    quantity = int(input("Enter Quantity: "))

    for p in products:

        if p["id"] == product_id:

            if quantity <= p["stock"]:

                bill = p["price"] * quantity
                p["stock"] -= quantity
                total_sales += bill

                print("Purchase successful")
                print("Bill =", bill)

            else:
                print("Insufficient stock")

            return

    print("Product not found")


# Update Product Price
def update_price():

    product_id = int(input("Enter Product ID: "))

    for p in products:

        if p["id"] == product_id:

            new_price = float(input("Enter New Price: "))
            p["price"] = new_price

            print("Price updated successfully")
            return

    print("Product not found")


# Sales Report
def sales_report():

    print("Total Sales = ₹", total_sales)


# Main Program
while True:

    print("\n------ SUPERMARKET MENU ------")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Purchase Product")
    print("5. Update Product Price")
    print("6. Sales Report")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_product()

    elif ch == 2:
        view_products()

    elif ch == 3:
        search_product()

    elif ch == 4:
        purchase_product()

    elif ch == 5:
        update_price()

    elif ch == 6:
        sales_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")