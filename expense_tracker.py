import csv

# Menu
def menu():
    print("\n----- Expense Tracker -----")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending by Date")
    print("4. Exit")
    print("5. Clear All Expenses")
    print("6. Delete Expense")
    print("7. Montly Spending Report")
    print("8. Category-wise Spending Report")


# Add Expense
def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("Expense added successfully!")


# View Expenses
def view_expenses():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            print("\nDate | Category | Amount | Description")
            print("---------------------------------------")

            for row in reader:
                if len(row)>=4:
                    print(row[0], "|", row[1], "|", row[2], "|", row[3])

    except FileNotFoundError:
        print("No expenses recorded.")


# Calculate Total by Date
def total_by_date():
    search_date = input("Enter date to calculate total (DD-MM-YYYY): ")

    total = 0

    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row)>0 and row[0] == search_date:
                    total += float(row[2])

        print("Total spending on", search_date, "=", total)

    except FileNotFoundError:
        print("No expenses recorded.")

# clear All Expenses

def clear_expenses():
    confirm = input("Are you sure you want to delete all expenses? (yes/no): ")

    if confirm.lower() == "yes":
        with open("expenses.csv", "w") as file:
            pass
        print("All expenses cleared successfully!")

    else:
        print("Operation cancelled.")

# delete expense

def delete_expense():
    date_delete = input("Enter the date of the expense (DD-MM-YYYY): ")

    print("\nDelete by:")
    print("1 Category")
    print("2 Description")
    print("3 Category and Description")

    option = input("Enter your choice: ")

    rows = []

    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            if option == "1":
                category_delete = input("Enter category: ").lower()

                for row in reader:
                    if len(row) >= 4 and not (row[0] == date_delete and row[1].lower() == category_delete):
                        rows.append(row)

            elif option == "2":
                description_delete = input("Enter description: ").lower()

                for row in reader:
                    if len(row) >= 4 and not (row[0] == date_delete and row[3].lower() == description_delete):
                        rows.append(row)

            elif option == "3":
                category_delete = input("Enter category: ").lower()
                description_delete = input("Enter description: ").lower()

                for row in reader:
                    if len(row) >= 4 and not (
                        row[0] == date_delete and
                        row[1].lower() == category_delete and
                        row[3].lower() == description_delete
                    ):
                        rows.append(row)

            else:
                print("Invalid choice")
                return

        with open("expenses.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print("Expense deleted successfully!")

    except FileNotFoundError:
        print("No expenses recorded.")

#monthly report        

def monthly_report():
    month = input("Enter month (MM): ")
    year = input("Enter year (YYYY): ")

    total = 0

    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) >= 4:
                    date = row[0]
                    amount = float(row[2])

                    day, m, y = date.split("-")

                    if m == month and y == year:
                        total += amount

        print(f"Total spending for {month}-{year}: {total}")

    except FileNotFoundError:
        print("No expenses recorded.")

# category_report

def category_report():
    category_totals = {}

    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) >= 4:
                    category = row[1]
                    amount = float(row[2])

                    if category in category_totals:
                        category_totals[category] += amount
                    else:
                        category_totals[category] = amount

        print("\nCategory-wise Spending Report")

        for category, total in category_totals.items():
            print(f"{category} : {total}")

    except FileNotFoundError:
        print("No expenses recorded.")

# Main Program
while True:
    menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_by_date()

    elif choice == "4":
        print("Goodbye!")
        break
    
    elif choice == "5":
        clear_expenses()
        
    elif choice =="6":
        delete_expense()

    elif choice =="7":
        monthly_report()

    elif choice =="8":
        category_report()

    else:
        print("Invalid choice")
