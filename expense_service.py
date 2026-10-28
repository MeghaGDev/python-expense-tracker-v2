
from models import Expense


def calculate_total(expenses: list[Expense]) -> float:
    """Return the total amount spent."""
    return sum(expense["amount"] for expense in expenses)


def filter_by_category(
    expenses: list[Expense],
    category: str
) -> list[Expense]:
    """Return expenses matching a category."""
    return [
        expense
        for expense in expenses
        if expense["category"].casefold() == category.strip().casefold()
    ]


def delete_expense(
    expenses: list[Expense],
    name: str
) -> bool:
    """Delete the first expense matching a name."""
    for index, expense in enumerate(expenses):
        if expense["name"].casefold() == name.strip().casefold():
            del expenses[index]
            return True

    return False
