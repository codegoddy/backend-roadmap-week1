# Backend Roadmap - Week 1, Day 3: Command-Line Applications

This folder contains a collection of small, interactive command-line interface (CLI) applications built with Python. The projects focus on fundamental concepts such as object-oriented programming (OOP), file I/O for data persistence, and robust error handling.

## Projects

### 1. Calculator App

A simple command-line calculator that performs basic arithmetic operations and keeps a history of all calculations.

- **File:** `calculator.py`
- **Data File:** `calc_history.txt`

**Features:**
- **Addition, Subtraction, Multiplication, Division:** Perform basic math operations.
- **View History:** Displays all past calculations with timestamps.
- **Error Handling:** Gracefully handles invalid number inputs and division by zero.

**How to Run:**
```bash
python calculator.py
```

### 2. Invoice Manager

A CLI tool for creating and viewing client invoices. Each invoice is saved to a text file.

- **Folder:** `invoice/`
- **File:** `invoice/invoice.py`
- **Data File:** `invoice/invoice.txt`

**Features:**
- **Add Invoice:** Prompts for client name, service type, and amount, then saves it.
- **View Invoices:** Lists all previously created invoices.
- **Data Persistence:** Invoices are stored with a timestamp and a paid/unpaid status marker.

**How to Run:**
```bash
python invoice/invoice.py
```

### 3. User Login & Registration System

A basic user authentication system that allows users to register for a new account and log in.

- **Folder:** `login/`
- **File:** `login/register_cli.py`
- **Data File:** `login/users.txt`

**Features:**
- **User Registration:** Creates a new user account by saving a username and password.
- **User Login:** Validates user credentials against the saved records.
- **File-Based Storage:** User data is stored in a simple comma-separated `users.txt` file.

**How to Run:**
```bash
python login/register_cli.py
```

### 4. Notes App

A full CRUD (Create, Read, Update, Delete) application for managing personal notes.

- **Folder:** `notes/`
- **File:** `notes/notes_cli.py`
- **Data File:** `notes/notes.txt`

**Features:**
- **Add Note:** Create a new note with a title and content.
- **View Notes:** Display all existing notes.
- **Update Note:** Modify the title or content of a specific note.
- **Delete Note:** Remove a note from the list.
- **Timestamping:** Notes are saved with the date and time of creation.

**How to Run:**
```bash
python notes/notes_cli.py
```

### 5. Simple Scripts

These files are smaller scripts used for practice and demonstration of specific concepts.

- **`warm_up.py`**: A basic script that demonstrates `try...except` blocks for handling `ValueError` and `ZeroDivisionError`.
- **`program.py`**: A script that performs division and logs the result to `results.txt` with a timestamp.

## Key Concepts Learned

- **Object-Oriented Programming (OOP):** Using classes (`Calculator`, `Invoice`, `User`, `Note`) to model real-world objects and organize code.
- **File I/O:** Reading from and writing to text files (`.txt`) to persist data between sessions.
- **Exception Handling:** Using `try...except` blocks to prevent crashes from invalid user input or logical errors (e.g., `ValueError`, `ZeroDivisionError`).
- **User Input:** Interacting with the user through the command line using the `input()` function.
- **Command-Line Interfaces (CLIs):** Structuring applications to run in a terminal, providing a menu of options for the user.
- **Date and Time:** Using the `datetime` module to create timestamps for records.
