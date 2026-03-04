# Quick-Calc

A simple command-line calculator application built for the Advanced Software Engineering course (Lecture 3 — Software Engineering & Testing). The focus of this project is not the UI, but the **quality of the code and its test suite**.

---

## Project Description

Quick-Calc supports five core operations:

| Operation      | Example          |
|----------------|-----------------|
| Addition       | 5 + 3 = 8       |
| Subtraction    | 10 − 4 = 6      |
| Multiplication | 6 × 7 = 42      |
| Division       | 10 ÷ 2 = 5      |
| Clear (C)      | Resets result to 0 |

Division by zero is handled gracefully — a `ValueError` is raised with a descriptive message instead of crashing.

---

## Setup Instructions

**Requirements:** Python 3.8 or higher.

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/swe-testing-assignment.git
   cd swe-testing-assignment
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the test dependency:
   ```bash
   pip install pytest
   ```

---

## How to Run Tests

Run the full test suite with a single command:

```bash
pytest test_calculator.py -v
```

The `-v` flag enables verbose output, showing each test name and its pass/fail status.

---

## Testing Framework Research

### Pytest vs Unittest

Python offers two widely used testing frameworks: **Pytest** and **Unittest**.

**Unittest** is part of the Python standard library, meaning it requires no installation. It follows an object-oriented structure inherited from Java's JUnit, where tests must be written inside classes that extend `unittest.TestCase`, and assertions use verbose methods like `self.assertEqual()` and `self.assertRaises()`. This makes it familiar to developers coming from statically typed languages, but adds boilerplate that can slow down writing tests.

**Pytest**, on the other hand, is a third-party framework that must be installed via pip, but it significantly reduces the amount of code required. Tests can be written as plain functions or inside classes without any special base class. Assertions use Python's native `assert` keyword, making tests more readable. Pytest also offers powerful features like fixtures, parametrize decorators, and detailed failure output with diffs, which help scale test suites efficiently.

**Choice for this project: Pytest.** For a project of this size and nature — focused on demonstrating a clean, readable test suite — Pytest is the superior choice. Its minimal syntax keeps the test file easy to read and grade, and its output format makes it immediately clear which tests pass or fail and why. Unittest would introduce unnecessary boilerplate without adding value here.

---

## Project Structure

```
swe-testing-assignment/
├── calculator.py        # Core calculator logic + input layer
├── test_calculator.py   # Full test suite (unit + integration)
├── README.md            # This file
└── TESTING.md           # Testing strategy and lecture concept analysis
```
