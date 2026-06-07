# Restaurant Order Management System

orders = []


# Add Order
def add_order():

    order_id = int(input("Enter Order ID: "))
    customer = input("Enter Customer Name: ")
    item = input("Enter Item (Pizza/Burger/Sandwich/Pasta): ")
    quantity = int(input("Enter Quantity: "))

    for o in orders:
        if o["id"] == order_id:
            print("Order ID already exists")
            return

    if item.lower() == "pizza":
        price = 200

    elif item.lower() == "burger":
        price = 120

    elif item.lower() == "sandwich":
        price = 100

    elif item.lower() == "pasta":
        price = 180

    else:
        print("Invalid Item")
        return

    total = price * quantity

    order = {
        "id": order_id,
        "customer": customer,
        "item": item,
        "quantity": quantity,
        "total": total
    }

    orders.append(order)

    print("Order added successfully")


# View Orders
def view_orders():

    if len(orders) == 0:
        print("No orders found")

    else:

        print("\n------ ORDER LIST ------")

        for o in orders:

            print("Order ID :", o["id"])
            print("Customer :", o["customer"])
            print("Item :", o["item"])
            print("Quantity :", o["quantity"])
            print("Total :", o["total"])
            print()


# Search Order
def search_order():

    order_id = int(input("Enter Order ID: "))

    for o in orders:

        if o["id"] == order_id:

            print("\nOrder Found")
            print("Customer :", o["customer"])
            print("Item :", o["item"])
            print("Quantity :", o["quantity"])
            print("Total :", o["total"])

            return

    print("Order not found")


# Update Order Quantity
def update_order():

    order_id = int(input("Enter Order ID: "))

    for o in orders:

        if o["id"] == order_id:

            new_qty = int(input("Enter New Quantity: "))

            if o["item"].lower() == "pizza":
                price = 200

            elif o["item"].lower() == "burger":
                price = 120

            elif o["item"].lower() == "sandwich":
                price = 100

            else:
                price = 180

            o["quantity"] = new_qty
            o["total"] = price * new_qty

            print("Order updated successfully")

            return

    print("Order not found")


# Cancel Order
def cancel_order():

    order_id = int(input("Enter Order ID: "))

    for o in orders:

        if o["id"] == order_id:

            orders.remove(o)

            print("Order cancelled successfully")

            return

    print("Order not found")


# Total Sales
def total_sales():

    sales = 0

    for o in orders:
        sales += o["total"]

    print("Total Sales =", sales)


# Main Program
while True:

    print("\n------ RESTAURANT MENU ------")
    print("1. Add Order")
    print("2. View Orders")
    print("3. Search Order")
    print("4. Update Order")
    print("5. Cancel Order")
    print("6. Total Sales")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_order()

    elif ch == 2:
        view_orders()

    elif ch == 3:
        search_order()

    elif ch == 4:
        update_order()

    elif ch == 5:
        cancel_order()

    elif ch == 6:
        total_sales()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")