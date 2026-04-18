def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, c):
    return a * c


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
