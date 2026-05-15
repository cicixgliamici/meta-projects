"""
This module represents "Pure Logic".
It has no dependencies on databases, network, or filesystem.
Because of this, it is perfectly suited for fast, isolated Unit Testing.
"""

def add(a: int, b: int) -> int:
    return a + b

def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
