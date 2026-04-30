seats = 10
bookings = {}

def check_availability():
    print("Available seats:", seats)

def view_ticket():
    bid = int(input("Enter booking ID: "))
    if bid in bookings:
        print(bookings[bid])
    else:
        print("Not found")

def cancel_ticket():
    global seats
    bid = int(input("Enter booking ID: "))
    if bid in bookings:
        del bookings[bid]
        seats += 1
        print("Cancelled")
    else:
        print("Not found")

while True:
    print("\n1.Check 2.View 3.Cancel 4.Exit")
    ch = input("Enter choice: ")
    
    if ch == "1":
        check_availability()
    elif ch == "2":
        view_ticket()
    elif ch == "3":
        cancel_ticket()
    elif ch == "4":
        break
