from expense import get_expenses
from budget import get_budget


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

    parts = month.strip().split()

    if len(parts) != 2:
        return None

    month_name = parts[0].lower()
    year = parts[1]

    if not year.isdigit() or len(year) != 4:
        return None

    month_number = months.get(month_name)

    if month_number is None:
        return None

    return f"{year}-{month_number}"


def calculate_total_expenses(month=None):
    """Calculate total expenses.

    month should be:
    September 2026

    If month is None, all expenses are included.
    """

    expenses = get_expenses()
    total = 0.0

    expense_month = None

    if month is not None:
        expense_month = convert_month_to_number(month)

        if expense_month is None:
            return 0.0

    for expense in expenses:

        if expense_month is None:
            total += float(expense["amount"])

        elif expense["date"].startswith(expense_month):
            total += float(expense["amount"])

    return total


def calculate_remaining_budget(month):
    """Calculate remaining budget for a month."""

    budget = get_budget(month)
    total_expenses = calculate_total_expenses(month)

    return budget - total_expenses


def calculate_budget_percentage(month):
    """Calculate percentage of budget used."""

    budget = get_budget(month)

    if budget <= 0:
        return 0.0

    total_expenses = calculate_total_expenses(month)

    return (total_expenses / budget) * 100


def get_budget_status(month):
    """Return the current budget status."""

    percentage = calculate_budget_percentage(month)

    if percentage < 80:
        return "GOOD"

    elif percentage < 100:
        return "WARNING"

    else:
        return "OVER BUDGET"


def display_calculation(month):
    """Display complete budget calculation."""

    budget = get_budget(month)
    total_expenses = calculate_total_expenses(month)
    remaining = calculate_remaining_budget(month)
    percentage = calculate_budget_percentage(month)
    status = get_budget_status(month)

    print("\n========== BUDGET SUMMARY ==========")
    print(f"Month              : {month}")
    print(f"Monthly Budget     : ₹{budget:.2f}")
    print(f"Total Expenses     : ₹{total_expenses:.2f}")
    print(f"Remaining Budget   : ₹{remaining:.2f}")
    print(f"Budget Used        : {percentage:.2f}%")
    print(f"Status             : {status}")
    print("====================================")


if __name__ == "__main__":

    month = input(
        "Enter month (e.g., September 2026): "
    ).strip()

    if convert_month_to_number(month) is None:
        print("Invalid month format.")
        print("Use format: September 2026")
    else:
        display_calculation(month)
