"""
Test suite for Quick-Calc.
Run with: pytest test_calculator.py -v
"""

import pytest
from calculator import Calculator


# ---------------------------------------------------------------------------
# UNIT TESTS
# Each test verifies a single function in isolation (white-box approach).
# ---------------------------------------------------------------------------

class TestAddition:
    """Unit tests for the add() method."""

    def test_add_two_positive_numbers(self):
        calc = Calculator()
        assert calc.add(5, 3) == 8

    def test_add_positive_and_negative(self):
        calc = Calculator()
        assert calc.add(10, -4) == 6

    def test_add_two_negative_numbers(self):
        calc = Calculator()
        assert calc.add(-7, -3) == -10


class TestSubtraction:
    """Unit tests for the subtract() method."""

    def test_subtract_two_positive_numbers(self):
        calc = Calculator()
        assert calc.subtract(10, 4) == 6

    def test_subtract_resulting_in_negative(self):
        calc = Calculator()
        assert calc.subtract(3, 10) == -7


class TestMultiplication:
    """Unit tests for the multiply() method."""

    def test_multiply_two_positive_numbers(self):
        calc = Calculator()
        assert calc.multiply(6, 7) == 42

    def test_multiply_by_zero(self):
        """Edge case: any number multiplied by zero must be zero."""
        calc = Calculator()
        assert calc.multiply(999, 0) == 0


class TestDivision:
    """Unit tests for the divide() method."""

    def test_divide_two_positive_numbers(self):
        calc = Calculator()
        assert calc.divide(10, 2) == 5.0

    def test_divide_by_zero_raises_error(self):
        """Edge case: division by zero must raise ValueError."""
        calc = Calculator()
        with pytest.raises(ValueError, match="Division by zero is not allowed."):
            calc.divide(8, 0)

    def test_divide_with_decimal_result(self):
        """Edge case: result should be a float when not evenly divisible."""
        calc = Calculator()
        assert calc.divide(7, 2) == 3.5

    def test_divide_very_large_numbers(self):
        """Edge case: verify correct handling of very large numbers."""
        calc = Calculator()
        assert calc.divide(1_000_000_000, 2) == 500_000_000.0


class TestClear:
    """Unit tests for the clear() method."""

    def test_clear_resets_result_to_zero(self):
        calc = Calculator()
        calc.result = 99
        calc.clear()
        assert calc.result == 0


# ---------------------------------------------------------------------------
# INTEGRATION TESTS
# Verify the interaction between the input layer and the calculation logic,
# simulating a real user session (black-box approach).
# ---------------------------------------------------------------------------

class TestIntegration:
    """Integration tests: input layer → calculation logic."""

    def test_full_user_interaction_addition(self):
        """
        Simulate: enter 5, press '+', enter 3, press '='.
        Expected result: 8.
        """
        calc = Calculator()
        calc.enter_number(5)
        calc.apply_operation("+", 3)
        assert calc.result == 8

    def test_clear_after_calculation_resets_to_zero(self):
        """
        Simulate: enter 10, press '*', enter 5, press 'C'.
        Expected result after clear: 0.
        """
        calc = Calculator()
        calc.enter_number(10)
        calc.apply_operation("*", 5)
        assert calc.result == 50      # verify calculation worked first
        calc.clear()
        assert calc.result == 0       # then verify clear resets to 0
