"""
Quick-Calc: A simple calculator application.
Supports addition, subtraction, multiplication, division, and clear.
"""


class Calculator:
    """A basic calculator with state (current result)."""

    def __init__(self):
        self.result = 0

    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the difference of a and b."""
        return a - b

    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b

    def divide(self, a, b):
        """
        Return the division of a by b.
        Raises ValueError if b is zero.
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    def clear(self):
        """Reset the current result to zero."""
        self.result = 0
        return self.result

    # --- Input layer (simulates user interaction) ---

    def enter_number(self, number):
        """Accept a number input from the user."""
        self.result = number
        return self.result

    def apply_operation(self, operator, number):
        """
        Apply an operation to the current result.
        Simulates pressing an operator button followed by a number.
        """
        if operator == "+":
            self.result = self.add(self.result, number)
        elif operator == "-":
            self.result = self.subtract(self.result, number)
        elif operator == "*":
            self.result = self.multiply(self.result, number)
        elif operator == "/":
            self.result = self.divide(self.result, number)
        else:
            raise ValueError(f"Unknown operator: {operator}")
        return self.result
