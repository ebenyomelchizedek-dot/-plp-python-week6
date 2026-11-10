# Python Week 6 Assignment – Safe Tools

## Assignment Description

This assignment demonstrates how Python handles errors using `try` and `except`.

## Files Included

- `safe_tools.py` – Contains three functions for safe division, number conversion, and dictionary field lookup.
- `README.md` – Provides an explanation of the assignment and its files.
- `week6_output.png` – Screenshot showing the program running successfully.

## Question: Why can the if check not catch abc on its own?

An `if` statement checks whether a condition is true or false, but it does not automatically catch errors that happen when converting text into a number. When Python tries to convert "abc" into an integer using `int()`, it raises a `ValueError`. We use `try` and `except` to catch this error and prevent the program from crashing.

## Expected Output

```text
5.0
Cannot divide by zero
42
Not a number
82
Field not found
```

## Conclusion

The assignment demonstrates how to use Python exception handling to make programs safer and more reliable.