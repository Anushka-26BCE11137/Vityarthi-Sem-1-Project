Personal Expense & Budget Tracker

1. Project Overview

The Personal Expense & Budget Tracker is a Python-based console application designed to help users record their daily expenses, set monthly budgets, and analyze their spending.

The application stores data using CSV files and provides useful information such as total expenses, remaining budget, budget usage percentage, category-wise spending, highest spending category, and budget warnings.

---

2. Objectives

The main objectives of this project are:

- To record personal expenses digitally.
- To maintain a monthly budget.
- To calculate total monthly expenses.
- To calculate the remaining budget.
- To analyze spending by category.
- To identify the highest spending category.
- To provide warnings when spending approaches or exceeds the budget.
- To store data permanently using CSV files.
- To demonstrate modular programming in Python.

---

3. Technologies Used

- Programming Language: Python
- Data Storage: CSV files
- Development Environment: Visual Studio Code
- Python Modules Used:
  - "csv"
  - "os"
  - "datetime"

No external Python libraries are required.

---

4. Features

4.1 Set Monthly Budget

The user can set a monthly budget.

Example:

Month: September 2026
Budget: ₹10,000

The budget is stored in "budget.csv".

4.2 Add Expense

The user can add an expense by entering:

- Date
- Category
- Description
- Amount

Example:

Date: 2026-09-28
Category: Food
Description: Dinner
Amount: ₹250

4.3 View Expenses

The application displays all stored expenses in a table.

4.4 View Budgets

The user can view all saved monthly budgets.

4.5 Budget Summary

The application calculates:

- Monthly budget
- Total expenses
- Remaining budget
- Percentage of budget used
- Budget status

4.6 Category Analysis

Expenses are grouped by category to show how much money is being spent on:

- Food
- Transport
- Education
- Entertainment
- Shopping
- Other categories

4.7 Highest Spending Category

The application identifies the category with the highest total spending.

4.8 Budget Warnings

The application provides spending alerts:

- Below 50% — spending is within the budget.
- 50% or more — spending notice.
- 80% or more — budget warning.
- 100% or more — budget exceeded.

---

5. Project Structure

Expense_Budget_Tracker/
│
├── main.py
├── expense.py
├── budget.py
├── calculator.py
├── analyzer.py
├── README.md
├── statement.md
│
└── data/
    ├── expenses.csv
    └── budget.csv

---

6. Description of Files

"main.py"

The main entry point of the application.

It:

- Displays the main menu.
- Takes user input.
- Calls functions from other modules.
- Controls the overall application flow.

"expense.py"

Handles expense-related operations.

It:

- Creates the expense CSV file.
- Adds expenses.
- Reads expenses.
- Displays expenses.
- Deletes all expenses.

"budget.py"

Handles budget-related operations.

It:

- Creates the budget CSV file.
- Sets monthly budgets.
- Updates existing budgets.
- Retrieves budgets.
- Displays saved budgets.

"calculator.py"

Performs financial calculations.

It calculates:

- Total expenses.
- Remaining budget.
- Budget usage percentage.
- Budget status.

It also converts a user-entered month such as:

September 2026

into:

2026-09

for expense filtering.

"analyzer.py"

Performs expense analysis.

It:

- Calculates category-wise expenses.
- Finds the highest spending category.
- Displays spending analysis.
- Displays budget warnings.

---

7. Data Storage

The application uses CSV files instead of a database.

"expenses.csv"

date,category,description,amount
2026-09-01,Food,Lunch,150
2026-09-02,Transport,Bus,50
2026-09-03,Education,Notebook,120
2026-09-28,Food,Dinner,250

"budget.csv"

month,budget
September 2026,10000

---

8. How to Run the Project

Step 1: Install Python

Make sure Python is installed on your computer.

Check the installation using:

python --version

Step 2: Open the Project

Open the "Expense_Budget_Tracker" folder in Visual Studio Code.

Step 3: Open the Terminal

In VS Code, open:

Terminal → New Terminal

Step 4: Run the Application

Execute:

python main.py

---

9. Main Menu

The application provides the following options:

========================================
      PERSONAL EXPENSE & BUDGET TRACKER
========================================
1. Set Monthly Budget
2. Add Expense
3. View Expenses
4. View Budgets
5. View Budget Summary
6. View Category Analysis
7. View Highest Spending Category
8. View Budget Warnings
9. Exit
========================================

---

10. Date and Month Formats

The application uses two formats:

Expense Date

YYYY-MM-DD

Example:

2026-09-28

Budget Month

Month YYYY

Example:

September 2026

The application internally converts the month into:

2026-09

when filtering expenses.

---

11. Testing

The following operations should be tested:

1. Set a monthly budget.
2. Add an expense.
3. Add multiple expenses.
4. View all expenses.
5. View saved budgets.
6. Calculate the budget summary.
7. Check category-wise spending.
8. Check the highest spending category.
9. Check budget warnings.
10. Restart the application and verify that CSV data is preserved.
11. Enter invalid dates.
12. Enter invalid amounts.
13. Enter empty categories.
14. Test spending above the monthly budget.

---

12. Advantages

- Simple and easy to use.
- No external libraries required.
- Data is stored permanently in CSV files.
- Modular Python code.
- Easy to maintain and extend.
- Provides basic spending analysis.
- Suitable for beginners learning Python.

---

13. Limitations

- It is a console-based application.
- It does not have a graphical user interface.
- CSV files are used instead of a database.
- It does not provide graphical charts.
- Individual expense editing and deletion are not currently included.

---

14. Future Enhancements

Possible future improvements include:

- Adding a graphical user interface using Tkinter.
- Adding charts and graphs.
- Adding individual expense editing and deletion.
- Adding search and filtering.
- Adding automatic monthly reports.
- Adding income tracking.
- Adding savings tracking.
- Adding export options.
- Using SQLite for more advanced data storage.
- Adding user accounts and authentication.

---

15. Conclusion

The Personal Expense & Budget Tracker demonstrates how Python can be used to build a practical financial management application.

The project combines Python functions, modules, conditional statements, loops, exception handling, CSV file handling, and basic data analysis into a single application.

It provides a simple way to record expenses, manage budgets, and understand spending patterns.