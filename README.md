

---

# Budget Planner – OOP Python Project

## Project Structure

```
budget_planner/
├── transaction.py
├── category.py
├── budget.py
├── main.py
└── README.md
```
## UML Diagram
<img width="6651" height="4263" alt="Untitled diagram-2025-12-25-173836" src="https://github.com/user-attachments/assets/80466a9a-fbfe-4886-a0ff-7acfd766391a" />

## How to Run

1. Make sure all files are in the same folder
2. Run the program using:

```
python main.py
```

## File Description

### transaction.py

Contains the abstract `Transaction` class and its subclasses:

* `Income`
* `Expense`

OOP concepts:

* Abstraction
* Inheritance
* Polymorphism

### category.py

Contains the `Category` class used to manage spending limits.

OOP concept:

* Encapsulation

### budget.py

Contains the `Budget` class which manages categories and transactions.

OOP concepts:

* Composition
* Polymorphism

### main.py

Contains the main program logic and user interface.

## OOP Concepts Used

1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism

## Features

* Create categories with spending limits
* Add income and expenses
* Calculate current balance
* Track spending per category
* Generate a monthly report

## Example Usage

1. Create a category called Food with a limit of 500
2. Add income of 2000
3. Add an expense of 50 under Food
4. Display balance and report

## Requirements

* Python 3.7 or higher
* No external libraries required
