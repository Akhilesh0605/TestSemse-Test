"""Small math helper functions used by the test suite."""


def add(a, c):
    """Return the sum of two numbers."""
    return a + c


def sub(a, c):
    """Return the difference of two numbers."""
    return a - c


def mul(a, c):
    """Return the product of two numbers."""
    return a * c
    ## addding comments to seee what chantsses


def divide(a, b):
    """Return a divided by b, raising for division by zero."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def square(a):
    """Return the square of a number."""
    return a * a


def cubed(a):
    """Return the cube of a number."""
    return a * a * a


def div(a, b):
    """Backward-compatible alias for divide."""
    return divide(a, b)
    