from expense import get_expenses
from calculator import (
    calculate_total_expenses,
    calculate_remaining_budget,
    calculate_budget_percentage,
    get_budget_status
)


def get_category_totals(month=None):
    """Calculate total spending for each category."""

    expenses = get_expenses()
    category_totals = {}

    for expense in expenses:

        # Filter expenses by month if a month is provided
        if month is not None:
            if not expense["date"].startswith(month):
                continue

        category = expense["category"]
        amount = float(expense["amount"])

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    return category_totals


def find_highest_category(month=None):
    """Find the category with the highest spending."""

    category_totals = get_category_totals(month)

    if not category_totals:
        return None, 0.0

    highest_category = max(
        category_totals,
        key=category_totals.get
    )

    highest_amount = category_totals[highest_category]

    return highest_category, highest_amount


def display_category_analysis(month=None):
    """Display category-wise expense analysis."""

    category_totals = get_category_totals(month)

    print("\n========== CATEGORY ANALYSIS ==========")

    if not category_totals:
        print("No expenses found.")
        return

    print(f"{'Category':<20}{'Amount':>15}")
    print("-" * 35)

    for category, amount in category_totals.items():
        print(f"{category:<20}₹{amount:>14.2f}")

    print("-" * 35)


def display_highest_category(month=None):
    """Display the category with the highest spending."""

    category, amount = find_highest_category(month)

    print("\n========== HIGHEST SPENDING ==========")

    if category is None:
        print("No expenses found.")
        return

    print(f"Category : {category}")
    print(f"Amount   : ₹{amount:.2f}")


def display_full_analysis(month):
    """Display a complete monthly expense analysis."""

    total_expenses = calculate_total_expenses(month)
    remaining_budget = calculate_remaining_budget(month)
    budget_percentage = calculate_budget_percentage(month)
    budget_status = get_budget_status(month)

    category_totals = get_category_totals(month)
    highest_category, highest_amount = find_highest_category(month)

    print("\n========================================")
    print("        PERSONAL EXPENSE ANALYSIS")
    print("========================================")

    print(f"\nMonth              : {month}")
    print(f"Total Expenses     : ₹{total_expenses:.2f}")
    print(f"Remaining Budget   : ₹{remaining_budget:.2f}")
    print(f"Budget Used        : {budget_percentage:.2f}%")
    print(f"Budget Status      : {budget_status}")

    print("\n---------- CATEGORY BREAKDOWN ----------")

    if category_totals:
        for category, amount in category_totals.items():
            print(f"{category:<20} ₹{amount:.2f}")
    else:
        print("No expenses found.")

    print("\n---------- HIGHEST SPENDING ----------")

    if highest_category:
        print(f"Category : {highest_category}")
        print(f"Amount   : ₹{highest_amount:.2f}")
    else:
        print("No expenses found.")

    print("========================================")


def show_spending_warnings(month):
    """Display warnings based on spending."""

    percentage = calculate_budget_percentage(month)

    print("\n---------- BUDGET ALERT ----------")

    if percentage >= 100:
        print("ALERT: You have exceeded your budget!")
    elif percentage >= 80:
        print("WARNING: You have used more than 80% of your budget.")
    elif percentage >= 50:
        print("NOTICE: You have used more than 50% of your budget.")
    else:
        print("Your spending is currently within a safe range.")

    print("----------------------------------")


if __name__ == "__main__":

    month = input(
        "Enter month (e.g., September 2026): "
    ).strip()

    display_full_analysis(month)
    show_spending_warnings(month)