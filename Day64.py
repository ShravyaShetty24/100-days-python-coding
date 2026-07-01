# Pharmacy Management System

medicines = []
total_sales = 0

# Add Medicine
def add_medicine():

    medicine_id = int(input("Enter Medicine ID: "))
    name = input("Enter Medicine Name: ")
    price = float(input("Enter Medicine Price: "))
    stock = int(input("Enter Stock Quantity: "))

    for m in medicines:
        if m["id"] == medicine_id:
            print("Medicine ID already exists")
            return

    medicine = {
        "id": medicine_id,
        "name": name,
        "price": price,
        "stock": stock,
        "sold": 0
    }

    medicines.append(medicine)
    print("Medicine added successfully")


# View Medicines
def view_medicines():

    if len(medicines) == 0:
        print("No medicines available")
    else:
        print("\n------ MEDICINE LIST ------")

        for m in medicines:
            print("ID :", m["id"])
            print("Name :", m["name"])
            print("Price :", m["price"])
            print("Stock :", m["stock"])
            print("Sold :", m["sold"])
            print()


# Search Medicine
def search_medicine():

    medicine_id = int(input("Enter Medicine ID: "))

    for m in medicines:
        if m["id"] == medicine_id:
            print("\nMedicine Found")
            print("Name :", m["name"])
            print("Price :", m["price"])
            print("Stock :", m["stock"])
            return

    print("Medicine not found")


# Sell Medicine
def sell_medicine():

    global total_sales

    medicine_id = int(input("Enter Medicine ID: "))
    quantity = int(input("Enter Quantity: "))

    for m in medicines:

        if m["id"] == medicine_id:

            if quantity <= m["stock"]:

                bill = quantity * m["price"]

                m["stock"] -= quantity
                m["sold"] += quantity
                total_sales += bill

                print("Medicine sold successfully")
                print("Bill = ₹", bill)

            else:
                print("Insufficient stock")

            return

    print("Medicine not found")


# Update Stock
def update_stock():

    medicine_id = int(input("Enter Medicine ID: "))

    for m in medicines:

        if m["id"] == medicine_id:

            new_stock = int(input("Enter New Stock: "))
            m["stock"] = new_stock

            print("Stock updated successfully")
            return

    print("Medicine not found")


# Sales Report
def sales_report():

    print("Total Sales = ₹", total_sales)

    total_sold = 0

    for m in medicines:
        total_sold += m["sold"]

    print("Total Medicines Sold =", total_sold)


# Main Program
while True:

    print("\n------ PHARMACY MENU ------")
    print("1. Add Medicine")
    print("2. View Medicines")
    print("3. Search Medicine")
    print("4. Sell Medicine")
    print("5. Update Stock")
    print("6. Sales Report")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_medicine()

    elif ch == 2:
        view_medicines()

    elif ch == 3:
        search_medicine()

    elif ch == 4:
        sell_medicine()

    elif ch == 5:
        update_stock()

    elif ch == 6:
        sales_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")