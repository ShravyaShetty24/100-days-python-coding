# Inventory Management System

products = []


# Function to add product
def add_product():

    product_id = int(input("Enter Product ID: "))
    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))
    stock = int(input("Enter Stock Quantity: "))

    # Check duplicate Product ID
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


# Function to view products
def view_products():

    if len(products) == 0:
        print("No products available")

    else:

        print("\n------ PRODUCT LIST ------")

        for p in products:

            print("Product ID :", p["id"])
            print("Name       :", p["name"])
            print("Price      :", p["price"])
            print("Stock      :", p["stock"])
            print()


# Function to search product
def search_product():

    product_id = int(input("Enter Product ID to search: "))

    for p in products:

        if p["id"] == product_id:

            print("\nProduct Found")
            print("Product ID :", p["id"])
            print("Name       :", p["name"])
            print("Price      :", p["price"])
            print("Stock      :", p["stock"])

            return

    print("Product not found")


# Function to update stock
def update_stock():

    product_id = int(input("Enter Product ID: "))

    for p in products:

        if p["id"] == product_id:

            new_stock = int(input("Enter New Stock Quantity: "))
            p["stock"] = new_stock

            print("Stock updated successfully")

            return

    print("Product not found")


# Function to delete product
def delete_product():

    product_id = int(input("Enter Product ID to delete: "))

    for p in products:

        if p["id"] == product_id:

            products.remove(p)

            print("Product deleted successfully")

            return

    print("Product not found")


# Function to calculate inventory value
def inventory_value():

    total = 0

    for p in products:
        total += p["price"] * p["stock"]

    print("\nTotal Inventory Value =", total)


# Main Program
while True:

    print("\n------ INVENTORY MENU ------")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Stock")
    print("5. Delete Product")
    print("6. Inventory Value")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_product()

    elif ch == 2:
        view_products()

    elif ch == 3:
        search_product()

    elif ch == 4:
        update_stock()

    elif ch == 5:
        delete_product()

    elif ch == 6:
        inventory_value()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")