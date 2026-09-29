import csv
import os
from datetime import datetime

FILE_PATH = "data/expenses.csv"


def initialize_file():
    """Create the expense CSV file if it does not exist."""

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "date",
                "category",
                "description",
                "amount"
            ])


def validate_date(date):
    """Check whether the date has YYYY-MM-DD format."""

    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True

    except ValueError:
        return False


def add_expense():
    """Take expense details and save them to the CSV file."""

    initialize_file()

    print("\n---------- ADD EXPENSE ----------")

    # Get date
    date = input(
        "Enter date (YYYY-MM-DD): "
    ).strip()

    if not validate_date(date):
        print("\nInvalid date.")
        print("Please use format: YYYY-MM-DD")
        return

    # Get category
    category = input(
        "Enter category: "
    ).strip()

    if category == "":
        print("Category cannot be empty.")
        return

    # Get description
    description = input(
        "Enter description: "
    ).strip()

    if description == "":
        print("Description cannot be empty.")
        return

    # Get amount
    try:
        amount = float(
            input("Enter amount: ₹")
        )

    except ValueError:
        print("Please enter a valid number.")
        return

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    # Save expense
    with open(FILE_PATH, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            date,
            category,
            description,
            amount
        ])

    print("\nExpense added successfully.")
    print(f"Date       : {date}")
    print(f"Category   : {category}")
    print(f"Description: {description}")
    print(f"Amount     : ₹{amount:.2f}")


def get_expenses():
    """Read all expenses from the CSV file."""

    initialize_file()

    expenses = []

    with open(FILE_PATH, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:
            expenses.append(row)

    return expenses


def view_expenses():
    """Display all saved expenses."""

    expenses = get_expenses()

    print("\n========== ALL EXPENSES ==========")

    if not expenses:
        print("No expenses found.")
        return

    print(
        f"{'Date':<15}"
        f"{'Category':<15}"
        f"{'Description':<25}"
        f"{'Amount':>10}"
    )

    print("-" * 65)

    for expense in expenses:

        amount = float(expense["amount"])

        print(
            f"{expense['date']:<15}"
            f"{expense['category']:<15}"
            f"{expense['description']:<25}"
            f"₹{amount:>9.2f}"
        )

    print("-" * 65)


def delete_all_expenses():
    """Delete all saved expenses."""

    initialize_file()

    with open(FILE_PATH, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "date",
            "category",
            "description",
            "amount"
        ])

    print("\nAll expenses have been deleted.")


if __name__ == "__main__":

    print("PERSONAL EXPENSE TRACKER")

    while True:

        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Delete All Expenses")
        print("4. Exit")

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            add_expense()

        elif choice == "2":

            view_expenses()

        elif choice == "3":

            confirmation = input(
                "Are you sure you want to delete "
                "all expenses? (yes/no): "
            ).strip().lower()

            if confirmation == "yes":
                delete_all_expenses()

            else:
                print("Deletion cancelled.")

        elif choice == "4":

            print("Exiting...")
            break

        else:

            print("Invalid choice.")
            