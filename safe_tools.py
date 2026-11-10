
# Function 1: Safe Division
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


# Function 2: Safe Number Conversion
def safe_number(text):
    try:
        return int(text)
    except ValueError:
        return "Not a number"


# Function 3: Get Dictionary Field
def get_field(learner, key):
    try:
        return learner[key]
    except KeyError:
        return "Field not found"


# Testing the three functions
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_number("42"))
print(safe_number("abc"))

learner = {"name": "Amina", "score": 82}
print(get_field(learner, "score"))
print(get_field(learner, "email"))
