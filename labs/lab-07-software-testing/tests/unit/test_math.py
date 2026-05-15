import pytest
import sys
import os

# Add src to the python path so we can import our modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from math_operations import add, divide

def test_add_positive_numbers():
    """Test pure logic. No mocks, no databases. Extremely fast."""
    assert add(2, 3) == 5

def test_divide_by_zero_raises_error():
    """Testing that our code correctly throws exceptions when expected."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
