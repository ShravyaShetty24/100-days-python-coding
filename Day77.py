# Event Registration Management System

events = []

# Add Event
def add_event():

    event_id = int(input("Enter Event ID: "))
    name = input("Enter Event Name: ")
    venue = input("Enter Venue: ")
    capacity = int(input("Enter Maximum Capacity: "))

    for e in events:
        if e["id"] == event_id:
            print("Event ID already exists")
            return

    event = {
        "id": event_id,
        "name": name,
        "venue": venue,
        "capacity": capacity,
        "registered": 0
    }

    events.append(event)
    print("Event added successfully")


# View Events
def view_events():

    if len(events) == 0:
        print("No events available")

    else:
        print("\n------ EVENT LIST ------")

        for e in events:
            print("Event ID :", e["id"])
            print("Event Name :", e["name"])
            print("Venue :", e["venue"])
            print("Capacity :", e["capacity"])
            print("Registered :", e["registered"])
            print()


# Search Event
def search_event():

    event_id = int(input("Enter Event ID: "))

    for e in events:

        if e["id"] == event_id:

            print("\nEvent Found")
            print("Name :", e["name"])
            print("Venue :", e["venue"])
            print("Capacity :", e["capacity"])
            print("Registered :", e["registered"])
            return

    print("Event not found")


# Register Participant
def register_participant():

    event_id = int(input("Enter Event ID: "))

    for e in events:

        if e["id"] == event_id:

            if e["registered"] < e["capacity"]:
                e["registered"] += 1
                print("Participant registered successfully")
            else:
                print("Event is full")

            return

    print("Event not found")


# Cancel Registration
def cancel_registration():

    event_id = int(input("Enter Event ID: "))

    for e in events:

        if e["id"] == event_id:

            if e["registered"] > 0:
                e["registered"] -= 1
                print("Registration cancelled successfully")
            else:
                print("No registrations to cancel")

            return

    print("Event not found")


# Event Report
def event_report():

    total_registered = 0

    for e in events:
        total_registered += e["registered"]

    print("Total Events =", len(events))
    print("Total Participants Registered =", total_registered)


# Main Program
while True:

    print("\n------ EVENT MANAGEMENT MENU ------")
    print("1. Add Event")
    print("2. View Events")
    print("3. Search Event")
    print("4. Register Participant")
    print("5. Cancel Registration")
    print("6. Event Report")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_event()

    elif ch == 2:
        view_events()

    elif ch == 3:
        search_event()

    elif ch == 4:
        register_participant()

    elif ch == 5:
        cancel_registration()

    elif ch == 6:
        event_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")