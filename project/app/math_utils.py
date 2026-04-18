def add(a, c):
    return a + c


def subtract(a, c):
    return a - c


def multiply(a, c):
    return a * c


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def square(a):
    return a*a
