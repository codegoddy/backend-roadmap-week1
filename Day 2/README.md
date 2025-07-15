# 🧠 Day 2 — Python Object-Oriented Programming (OOP)

This document covers my progress on Day 2 of the **14-Week Backend + DevOps Developer Roadmap**. The focus today was on shifting from procedural programming to Object-Oriented Programming (OOP) using Python.

---

## ✅ What I Learned Today

Today was all about understanding the core principles of OOP and how to apply them to build more structured, scalable, and reusable code.

- **Classes and Objects:** Learned to define a `class` as a blueprint and create `objects` (instances) from it.
- **The `__init__()` Method:** Understood its role as a constructor to initialize an object's attributes when it's created.
- **The `self` Keyword:** Got comfortable with `self` as a reference to the current instance of a class, allowing access to its attributes and methods.
- **Attributes and Methods:** Differentiated between attributes (data/state, e.g., `book.title`) and methods (behavior/functions, e.g., `book.display()`).
- **Encapsulation:** Grasped the concept of bundling data and the methods that operate on that data within a single unit (the class). This helps in hiding internal complexity.
- **Class Interaction:** Built applications where different classes work together. For example, a `BookTracker` class that manages a list of `Book` objects.

---

## 🚀 Projects Built

I applied OOP concepts to build and refactor several practical command-line applications.

### 1. `oops.py` & `developer.py`

Simple introductory scripts to practice the basics of class creation.

- `oops.py`: A basic `Dog` class to demonstrate creating a class, initializing it, and calling its methods.
- `developer.py`: A `Developer` class with attributes like `name` and `level`, and methods like `promote()` that modify the object's state.

---

### 2. `taskmanager.py`

An OOP-based Task Manager that refactors the logic from Day 1 into a more robust structure.

**Features:**

- A `Task` class to represent individual tasks with properties like `name`, `time_estimate`, and `is_completed`.
- A `TaskManager` class to handle the application logic: adding, viewing, completing, and removing tasks.
- Demonstrates how one class (`TaskManager`) can manage a collection of objects of another class (`Task`).

---

### 3. `habit_tracker.py`

A rewrite of the Day 1 habit tracker using an object-oriented approach.

**Features:**

- A `Habit` class to store the `name` and completion status (`is_done`) of a habit.
- A `HabitTracker` class that contains a list of `Habit` objects and provides methods to `add_habit`, `view_habits`, `mark_done`, and show a `summary`.
- Cleaner separation of concerns compared to the procedural version.

---

### 4. `expense_tracker.py`

An OOP version of the Day 1 expense tracker, built to manage spending.

**Features:**

- An `Expense` class to model each spending event with a `description` and `amount`.
- An `ExpenseTracker` class to add, view, and summarize expenses.
- The summary calculates the total number of expenses, the total amount spent, and identifies the single largest expense.

---

### 5. `book_tracker.py`

A new CLI application to log and manage a reading list.

**Features:**

- `Book` class with attributes for `title`, `author`, `pages`, and `rating`.
- `BookTracker` class to manage the collection of books.
- Functionality to add books, view the list, and calculate a summary (total books, total pages, average rating).
- Includes robust error handling for user input.

---

## 📝 Why This Matters

Object-Oriented Programming is a fundamental paradigm in modern software development, especially for backend systems.

- **Organization:** OOP helps organize complex systems into logical, manageable, and reusable components (classes).
- **Scalability:** Well-structured classes make it easier to add new features and maintain the codebase as it grows.
- **Modeling the Real World:** OOP is excellent for modeling real-world entities, which is core to backend development (e.g., `User`, `Product`, `Order` models in an e-commerce API).
- **Foundation for Frameworks:** Most backend frameworks (like Django, Flask, FastAPI) are built on OOP principles. Understanding classes is essential for using them effectively.

---
