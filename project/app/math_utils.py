def add(a, c):
    return a + c


def sub(a, c):
    return a - c


def mul(a, c):
    return a * c


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def square(a):
    return a*a
