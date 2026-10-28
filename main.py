
from models import Expense
from storage import load_expenses, save_expenses
from expense_service import (
    calculate_total,
    filter_by_category,
    delete_expense,
)


def add_expense(expenses: list[Expense]) -> None:
    name = input("Enter expense name: ").strip()

    if not name:
        print("Expense name cannot be empty!")
        return

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Please enter a valid number!")
        return

    if amount <= 0:
        print("Amount must be greater than zero!")
        return

    category = input("Enter category: ").strip()

    if not category:
        print("Category cannot be empty!")
        return

    expense: Expense = {
        "name": name,
        "amount": amount,
        "category": category,
    }

    expenses.append(expense)
    save_expenses(expenses)
    print(f"{name} added successfully!")


def view_expenses(expenses: list[Expense]) -> None:
    if not expenses:
        print("No expenses found!")
        return

    for item in expenses:
        print(f"Name: {item['name']}")
        print(f"Amount: ₹{item['amount']:.2f}")
        print(f"Category: {item['category']}")
        print("----------------------")


def show_total(expenses: list[Expense]) -> None:
    total = calculate_total(expenses)
    print(f"Total spending: ₹{total:.2f}")


def show_category(expenses: list[Expense]) -> None:
    category = input("Enter category to check: ").strip()
    matches = filter_by_category(expenses, category)

    if not matches:
        print("No expenses found for this category!")
        return

    for item in matches:
        print(
            f"{item['name']} - ₹{item['amount']:.2f} "
            f"({item['category']})"
        )


def remove_expense(expenses: list[Expense]) -> None:
    name = input("Enter expense name to delete: ").strip()

    if delete_expense(expenses, name):
        save_expenses(expenses)
        print(f"{name} deleted successfully!")
    else:
        print("Expense not found!")


def main() -> None:
    expenses = load_expenses()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Spending")
        print("4. Filter by Category")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            show_category(expenses)
        elif choice == "5":
            remove_expense(expenses)
        elif choice == "6":
            print("Exiting Expense Tracker!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
