from expense import add_expense, view_expenses
from budget import set_budget, view_budgets
from calculator import (
    calculate_total_expenses,
    calculate_remaining_budget,
    calculate_budget_percentage,
    get_budget_status
)
from analyzer import (
    display_category_analysis,
    display_highest_category,
    show_spending_warnings
)


def display_menu():
    """Display the main menu."""

    print("\n")
    print("========================================")
    print("      PERSONAL EXPENSE & BUDGET TRACKER")
    print("========================================")
    print("1. Set Monthly Budget")
    print("2. Add Expense")
    print("3. View Expenses")
    print("4. View Budgets")
    print("5. View Budget Summary")
    print("6. View Category Analysis")
    print("7. View Highest Spending Category")
    print("8. View Budget Warnings")
    print("9. Exit")
    print("========================================")


def get_month():
    """Get the month from the user."""

    return input(
        "\nEnter month (e.g., September 2026): "
    ).strip()


def show_budget_summary():
    """Display budget and expense summary."""

    month = get_month()

    if not month:
        print("Month cannot be empty.")
        return

    total_expenses = calculate_total_expenses(
        convert_month_to_number(month)
    )

    remaining_budget = calculate_remaining_budget(month)
    percentage = calculate_budget_percentage(month)
    status = get_budget_status(month)

    print("\n========== BUDGET SUMMARY ==========")
    print(f"Month              : {month}")
    print(f"Total Expenses     : ₹{total_expenses:.2f}")
    print(f"Remaining Budget   : ₹{remaining_budget:.2f}")
    print(f"Budget Used        : {percentage:.2f}%")
    print(f"Budget Status      : {status}")
    print("====================================")


def convert_month_to_number(month):
    """Convert 'September 2026' to '2026-09'."""

    months = {
        "january": "01",
        "february": "02",
        "march": "03",
        "april": "04",
        "may": "05",
        "june": "06",
        "july": "07",
        "august": "08",
        "september": "09",
        "october": "10",
        "november": "11",
        "december": "12"
    }

    parts = month.split()

    if len(parts) != 2:
        return ""

    month_name = parts[0].lower()
    year = parts[1]

    month_number = months.get(month_name)

    if month_number is None:
        return ""

    return f"{year}-{month_number}"


def main():
    """Run the Expense & Budget Tracker."""

    while True:

        display_menu()

        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            set_budget()

        elif choice == "2":
            add_expense()

        elif choice == "3":
            view_expenses()

        elif choice == "4":
            view_budgets()

        elif choice == "5":
            show_budget_summary()

        elif choice == "6":
            month = get_month()

            if month:
                expense_month = convert_month_to_number(month)
                display_category_analysis(expense_month)
            else:
                print("Invalid month.")

        elif choice == "7":
            month = get_month()

            if month:
                expense_month = convert_month_to_number(month)
                display_highest_category(expense_month)
            else:
                print("Invalid month.")

        elif choice == "8":
            month = get_month()

            if month:
                show_spending_warnings(
                    month
                )
            else:
                print("Invalid month.")

        elif choice == "9":
            print("\nThank you for using Personal Expense & Budget Tracker.")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice.")
            print("Please select a number between 1 and 9.")


if __name__ == "__main__":
    main()