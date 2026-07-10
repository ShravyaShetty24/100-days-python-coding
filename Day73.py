# Restaurant Order Management System

menu = []
total_sales = 0

# Add Menu Item
def add_item():

    item_id = int(input("Enter Item ID: "))
    name = input("Enter Item Name: ")
    price = float(input("Enter Item Price: "))

    for item in menu:
        if item["id"] == item_id:
            print("Item ID already exists")
            return

    item = {
        "id": item_id,
        "name": name,
        "price": price,
        "sold": 0
    }

    menu.append(item)
    print("Menu item added successfully")


# View Menu
def view_menu():

    if len(menu) == 0:
        print("No menu items available")

    else:
        print("\n------ MENU ------")

        for item in menu:
            print("ID :", item["id"])
            print("Name :", item["name"])
            print("Price : ₹", item["price"])
            print("Sold :", item["sold"])
            print()


# Search Menu Item
def search_item():

    item_id = int(input("Enter Item ID: "))

    for item in menu:

        if item["id"] == item_id:

            print("\nItem Found")
            print("Name :", item["name"])
            print("Price : ₹", item["price"])
            print("Sold :", item["sold"])
            return

    print("Item not found")


# Place Order
def place_order():

    global total_sales

    item_id = int(input("Enter Item ID: "))
    quantity = int(input("Enter Quantity: "))

    for item in menu:

        if item["id"] == item_id:

            bill = item["price"] * quantity
            item["sold"] += quantity
            total_sales += bill

            print("Order placed successfully")
            print("Bill = ₹", bill)
            return

    print("Item not found")


# Update Item Price
def update_price():

    item_id = int(input("Enter Item ID: "))

    for item in menu:

        if item["id"] == item_id:

            new_price = float(input("Enter New Price: "))
            item["price"] = new_price

            print("Price updated successfully")
            return

    print("Item not found")


# Sales Report
def sales_report():

    total_items = 0

    for item in menu:
        total_items += item["sold"]

    print("Total Menu Items =", len(menu))
    print("Total Items Sold =", total_items)
    print("Total Sales = ₹", total_sales)


# Main Program
while True:

    print("\n------ RESTAURANT MENU ------")
    print("1. Add Menu Item")
    print("2. View Menu")
    print("3. Search Menu Item")
    print("4. Place Order")
    print("5. Update Item Price")
    print("6. Sales Report")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_item()

    elif ch == 2:
        view_menu()

    elif ch == 3:
        search_item()

    elif ch == 4:
        place_order()

    elif ch == 5:
        update_price()

    elif ch == 6:
        sales_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")