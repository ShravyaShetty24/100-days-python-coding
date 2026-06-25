foods = []

# Add Food Item
def add_food():

    food_id = int(input("Enter Food ID: "))
    name = input("Enter Food Name: ")
    price = float(input("Enter Price: "))

    food = {
        "id": food_id,
        "name": name,
        "price": price,
        "orders": 0
    }

    foods.append(food)

    print("Food item added successfully")


# View Food Items
def view_foods():

    if len(foods) == 0:
        print("No food items available")

    else:
        for f in foods:
            print("\nID :", f["id"])
            print("Name :", f["name"])
            print("Price :", f["price"])


# Search Food Item
def search_food():

    food_id = int(input("Enter Food ID: "))

    for f in foods:
        if f["id"] == food_id:
            print("Food Found")
            print("Name :", f["name"])
            print("Price :", f["price"])
            return

    print("Food item not found")


# Place Order
def place_order():

    food_id = int(input("Enter Food ID: "))
    qty = int(input("Enter Quantity: "))

    for f in foods:
        if f["id"] == food_id:

            bill = f["price"] * qty
            f["orders"] += qty

            print("Order placed successfully")
            print("Bill =", bill)

            return

    print("Food item not found")


# Cancel Order
def cancel_order():

    food_id = int(input("Enter Food ID: "))
    qty = int(input("Enter Quantity to Cancel: "))

    for f in foods:
        if f["id"] == food_id:

            if qty <= f["orders"]:
                f["orders"] -= qty
                print("Order cancelled successfully")
            else:
                print("Invalid quantity")

            return

    print("Food item not found")


# Sales Report
def sales_report():

    total_orders = 0

    for f in foods:
        total_orders += f["orders"]

    print("Total Food Orders =", total_orders)


# Main Program
while True:

    print("\n----- FOOD DELIVERY MENU -----")
    print("1. Add Food Item")
    print("2. View Food Items")
    print("3. Search Food Item")
    print("4. Place Order")
    print("5. Cancel Order")
    print("6. Sales Report")
    print("7. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        add_food()

    elif ch == 2:
        view_foods()

    elif ch == 3:
        search_food()

    elif ch == 4:
        place_order()

    elif ch == 5:
        cancel_order()

    elif ch == 6:
        sales_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")