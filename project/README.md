# Simple Python Coverage Demo

This project is a small Python example for testing a diff-based coverage tool such as TestSense.

## Project Structure

```text
project/
├── app/
│   ├── __init__.py
│   ├── math_utils.py
│   ├── string_utils.py
├── tests/
│   ├── test_math_utils.py
│   ├── test_string_utils.py
├── requirements.txt
├── README.md
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Tests

```bash
pytest
```

## Generate Coverage XML

```bash
pytest --cov=app --cov-report=xml
```

This creates a `coverage.xml` file in the project root.

## Coverage Notes

The test suite is intentionally mixed so you can simulate different coverage levels:

- Some functions are fully covered.
- Some functions are only partially covered.
- At least one function (`is_palindrome`) is left completely untested.

That makes the project useful for diff-based coverage experiments.
