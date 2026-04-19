import pytest

from app.math_utils import add, divide, mul, sub,cube,square


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert sub(10, 4) == 6
    assert sub(0, 5) == -5


def test_multiply():
    assert mul(3, 4) == 12
    assert mul(-2, 5) == -10


def test_divide_normal_case():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

def test_square():
    assert square(2)==4

def test_cube():
    assert cube(2)==8
