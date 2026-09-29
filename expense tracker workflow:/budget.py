import csv
import os

FILE_PATH = "data/budget.csv"


def initialize_file():
    """Create the budget CSV file if it does not exist."""

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["month", "budget"])


def set_budget():
    """Set or update the monthly budget."""

    initialize_file()

    print("\n---------- SET BUDGET ----------")

    month = input(
        "Enter month (e.g., September 2026): "
    ).strip()

    if month == "":
        print("Month cannot be empty.")
        return

    try:
        amount = float(
            input("Enter monthly budget: ₹")
        )
    except ValueError:
        print("Please enter a valid number.")
        return

    if amount <= 0:
        print("Budget must be greater than zero.")
        return

    budgets = []

    with open(FILE_PATH, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            budgets.append(row)

    month_found = False

    for budget in budgets:
        if budget["month"].lower() == month.lower():
            budget["budget"] = str(amount)
            month_found = True

    if not month_found:
        budgets.append({
            "month": month,
            "budget": str(amount)
        })

    with open(FILE_PATH, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["month", "budget"]
        )

        writer.writeheader()
        writer.writerows(budgets)

    if month_found:
        print(f"\nBudget for {month} updated successfully.")
    else:
        print(f"\nBudget for {month} set successfully.")

    print(f"Monthly Budget: ₹{amount:.2f}")


def get_budget(month):
    """Return the budget for a specific month.

    Month format:
    September 2026
    """

    initialize_file()

    with open(FILE_PATH, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["month"].lower() == month.lower():
                return float(row["budget"])

    return 0.0


def view_budgets():
    """Display all saved monthly budgets."""

    initialize_file()

    print("\n========== SAVED BUDGETS ==========")

    budgets_found = False

    with open(FILE_PATH, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            budgets_found = True

            print(
                f"{row['month']:<20}"
                f"₹{float(row['budget']):>10.2f}"
            )

    if not budgets_found:
        print("No budgets found.")

    print("-" * 35)


def delete_all_budgets():
    """Delete all saved budgets."""

    initialize_file()

    with open(FILE_PATH, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["month", "budget"])

    print("\nAll budgets have been deleted.")


if __name__ == "__main__":
    set_budget()
    view_budgets()
