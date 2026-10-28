# Expense Tracker V2

A command-line expense tracking application built with Python. This version focuses on improving code organization, maintainability, type hints, input validation, and JSON-based persistence.

## Features

- Add expenses with a name, amount, and category
- View all saved expenses
- Calculate total spending
- Filter expenses by category
- Delete expenses by name
- Persist expense records using JSON
- Validate user input and handle invalid JSON files
- Use type hints to document function parameters and return values
- Separate application logic, storage, and data definitions into modules

## Tech Stack

- Python 3.10+
- JSON for local data persistence
- Python standard library
- Type hints and `TypedDict`

## Project Structure

```text
expense_tracker_v2/
├── main.py
├── models.py
├── expense_service.py
├── storage.py
└── expense.json
```

- `main.py` — command-line menu and user interaction
- `models.py` — expense data structure using `TypedDict`
- `expense_service.py` — expense calculations, filtering, and deletion
- `storage.py` — JSON loading and saving
- `expense.json` — locally persisted expense data

## Getting Started

1. Install Python 3.10 or later.
2. Clone the repository.
3. Open a terminal in the `expense_tracker_v2` directory.
4. Run the application:

```bash
python main.py
```

## Learning Objectives

This project demonstrates practical use of:

- Python modules and imports
- Functions and type hints
- Lists and dictionaries
- Input validation and exception handling
- JSON file handling
- Separation of concerns
- Reusable business logic

## Future Improvements

- Automated tests using pytest
- Stronger data validation
- CSV export
- Unit tests for expense operations
- Database integration with PostgreSQL
- A FastAPI backend

## Project Status

In progress — built as part of my journey toward Python backend development.

