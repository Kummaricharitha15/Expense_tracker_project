import datetime

FILE_NAME = "expenses.txt"

def add_expense():
    amount = float(input("Enter amount: "))
    desc = input("Enter description: ")
    date = datetime.date.today().isoformat()

    with open(FILE_NAME, "a") as f:
        f.write(f"{date}|{amount}|{desc}\n")

    print("Expense added!")

def view_todays_expenses():
    today = datetime.date.today().isoformat()
    print(f"\n--- Expenses for {today} ---")
    found = False
    with open(FILE_NAME, "r") as f:
        for line in f:
            date, amount, desc = line.strip().split("|")
            if date == today:
                print(f"{desc} - ₹{amount}")
                found = True
    if not found:
        print("No expenses for today.")

def view_all_expenses():
    print("\n--- All Expenses ---")
    with open(FILE_NAME, "r") as f:
        data = f.readlines()
        if not data:
            print("No expenses found.")
            return
        for line in data:
            date, amount, desc = line.strip().split("|")
            print(f"{date} - {desc} - ₹{amount}")

def total_today():
    today = datetime.date.today().isoformat()
    total = 0
    with open(FILE_NAME, "r") as f:
        for line in f:
            date, amount, desc = line.strip().split("|")
            if date == today:
                total += float(amount)
    print(f"\nTotal spent today: ₹{total}")

def total_all_days():
    total = 0
    with open(FILE_NAME, "r") as f:
        for line in f:
            date, amount, desc = line.strip().split("|")
            total += float(amount)
    print(f"\nTotal spent overall: ₹{total}")

def show_menu():
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Today’s Expenses")
    print("3. View All Expenses")
    print("4. Total Today")
    print("5. Total All Days")
    print("6. Exit")

# Ensure file exists
open(FILE_NAME, "a").close()

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_todays_expenses()
    elif choice == "3":
        view_all_expenses()
    elif choice == "4":
        total_today()
    elif choice == "5":
        total_all_days()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
