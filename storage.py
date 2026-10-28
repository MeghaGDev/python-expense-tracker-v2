import json 
from pathlib import Path
from models import Expense



BASE_DIR = Path(__file__).resolve().parent
JSON_FILE = BASE_DIR/"expense.json"


def load_expenses() -> list[Expense]:
    """Load expenses from JSON, or return an empty list."""

    try:
        with open(JSON_FILE,"r",encoding="utf-8") as file :
            data = json.load(file)
    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Warning:expense.json contain invalid Json")
        return []

    if not isinstance(data,list):
        print("Warning: expense.json must contain a list.")
        return []

    expenses: list[Expense] = []


    for item in data:
        if (
            isinstance(item, dict)
            and isinstance(item.get("name"), str)
            and isinstance(item.get("amount"), (int, float))
            and not isinstance(item.get("amount"), bool)
            and isinstance(item.get("category"), str)
        ):
            expenses.append({
                "name": item["name"],
                "amount": float(item["amount"]),
                "category": item["category"]
            })

    return expenses


def save_expenses(expenses: list[Expense]) -> None:
    """Save expenses to JSON."""
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


