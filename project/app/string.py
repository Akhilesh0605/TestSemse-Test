"""String helper functions used by the test suite."""


def to_upper(text):
    """Return text converted to uppercase."""
    return text.upper()


def to_lower(text):
    """Return text converted to lowercase."""
    return text.lower()


def reverse_string(text):
    """Return text with characters in reverse order."""
    return text[::-1]


def is_palindrome(text):
    """Return True if text is a palindrome (ignoring spaces and case)."""
    cleaned = "".join(text.lower().split())
    return cleaned == cleaned[::-1]
