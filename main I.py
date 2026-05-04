import os

# Total seats
seats = 10

# Predefined bookings (since booking feature is removed)
bookings = {
    1: {"name": "Akhil", "age": 18},
    2: {"name": "Rahul", "age": 20}
}

# Clear screen function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Header UI
def header():
    print("=" * 40)
    print("     RAILWAY RESERVATION SYSTEM")
    print("=" * 40)

# Check seat availability
def check_availability():
    print("\nAvailable Seats:", seats)

# View ticket details
def view_ticket():
    try:
        bid = int(input("\nEnter Booking ID: "))
        if bid in bookings:
            print("\nTicket Details")
            print("-" * 20)
            print("Booking ID:", bid)
            print("Name      :", bookings[bid]["name"])
            print("Age       :", bookings[bid]["age"])
        else:
            print("Booking not found")
    except:
        print("Invalid input")

# Cancel ticket
def cancel_ticket():
    global seats
    try:
        bid = int(input("\nEnter Booking ID to cancel: "))
        if bid in bookings:
            del bookings[bid]
            seats += 1
            print("Ticket cancelled successfully")
        else:
            print("Booking not found")
    except:
        print("Invalid input")

# Main program loop
while True:
    clear()
    header()

    print("\n1. Check Availability")
    print("2. View Ticket")
    print("3. Cancel Ticket")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        check_availability()
    elif choice == "2":
        view_ticket()
    elif choice == "3":
        cancel_ticket()
    elif choice == "4":
        print("\nExiting program...")
        break
    else:
        print("Invalid choice")

    input("\nPress Enter to continue...")
