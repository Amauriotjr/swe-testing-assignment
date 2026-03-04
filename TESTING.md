# TESTING.md — Testing Strategy for Quick-Calc

## Testing Strategy

### What Was Tested

The test suite covers all four core calculation operations (addition, subtraction, multiplication, and division) as well as the clear function and the input layer (the `enter_number` and `apply_operation` methods). Within each operation, at least one standard case and one or more edge cases were included.

The edge cases tested are:
- **Division by zero** — the most critical edge case, where the application must fail gracefully with a meaningful error rather than crashing.
- **Multiplication by zero** — any number multiplied by zero must return zero.
- **Decimal results** — dividing numbers that don't divide evenly must return a correct float (e.g., 7 ÷ 2 = 3.5).
- **Very large numbers** — verifying the calculator handles inputs like 1,000,000,000 without overflow errors.
- **Negative numbers** — operations involving negative operands to ensure signed arithmetic is correct.

### What Was Not Tested (and Why)

Non-functional aspects such as **performance** (response time under load), **security**, and **cross-platform compatibility** were not tested. For a CLI calculator of this scope, these are not meaningful concerns — the application has no network surface, no persistent storage, and no concurrent users. Testing them would add complexity without adding real value.

UI-level tests were also excluded, because the assignment explicitly states that the focus is *not* on the UI. The `apply_operation` method acts as the boundary between the input layer and the logic layer, and integration tests verify this boundary directly.

---

## Lecture Concepts Applied

### 1. The Testing Pyramid

The Testing Pyramid recommends having many unit tests at the base, fewer integration tests in the middle, and even fewer system/end-to-end tests at the top. This project follows that structure: there are **11 unit tests** (base) and **2 integration tests** (middle). System and acceptance testing were not applicable for this scope, maintaining the pyramid's proportions and keeping the suite fast and focused.

### 2. Black-box vs White-box Testing

**Unit tests** in this project use a **white-box** approach — the tests were written with direct knowledge of the internal implementation. For example, knowing that `divide()` raises a `ValueError` for zero was informed by reading the source code, and the test directly checks for that specific exception type and message.

**Integration tests** use a **black-box** approach — they interact with the calculator through the public input layer (`enter_number`, `apply_operation`, `clear`) without caring about how the underlying methods are implemented internally. The tester only specifies input and expected output, just like a real user would.

### 3. Functional vs Non-Functional Testing

All tests in this suite are **functional tests** — they verify that the calculator *does what it is supposed to do* according to the requirements in Section 2 of the assignment. For example, "correctly adds two numbers" and "handles division by zero gracefully" are functional requirements.

**Non-functional testing** (e.g., performance, scalability, security) was intentionally excluded, as described in the strategy section above. This reflects the concept that functional testing validates *correctness*, while non-functional testing validates *quality attributes* — and for this application, functional correctness is the primary concern.

### 4. Regression Testing

The existing test suite serves directly as a **regression test suite**. Every time a new feature is added or a bug is fixed in `calculator.py`, running `pytest test_calculator.py -v` will immediately reveal whether any previously working functionality has broken. For example, if a future developer modifies the `divide()` method and accidentally removes the zero-check, the `test_divide_by_zero_raises_error` test will fail immediately, catching the regression before it reaches production.

---

## Test Results Summary

| Test Name                                   | Type        | Status |
|---------------------------------------------|-------------|--------|
| test_add_two_positive_numbers               | Unit        | ✅ Pass |
| test_add_positive_and_negative              | Unit        | ✅ Pass |
| test_add_two_negative_numbers               | Unit        | ✅ Pass |
| test_subtract_two_positive_numbers          | Unit        | ✅ Pass |
| test_subtract_resulting_in_negative         | Unit        | ✅ Pass |
| test_multiply_two_positive_numbers          | Unit        | ✅ Pass |
| test_multiply_by_zero                       | Unit        | ✅ Pass |
| test_divide_two_positive_numbers            | Unit        | ✅ Pass |
| test_divide_by_zero_raises_error            | Unit        | ✅ Pass |
| test_divide_with_decimal_result             | Unit        | ✅ Pass |
| test_divide_very_large_numbers              | Unit        | ✅ Pass |
| test_clear_resets_result_to_zero            | Unit        | ✅ Pass |
| test_full_user_interaction_addition         | Integration | ✅ Pass |
| test_clear_after_calculation_resets_to_zero | Integration | ✅ Pass |
