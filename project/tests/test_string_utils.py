from app.string_utils import reverse_string, to_lower, to_upper


def test_to_upper():
    assert to_upper("hello") == "HELLO"
    assert to_upper("PyTeSt") == "PYTEST"


def test_to_lower():
    assert to_lower("HELLO") == "hello"
    assert to_lower("PyTeSt") == "pytest"


def test_reverse_string():
    assert reverse_string("abcd") == "dcba"
    assert reverse_string("Test") == "tseT"
