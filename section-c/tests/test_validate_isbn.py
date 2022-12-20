"""Test eyesbeen validation"""
import pytest

from eyesbeen import validate_isbn

test_cases = [
    ("031606652X", "Invalid"),
    ("0316X6652X", "Invalid"),
    ("0330301824", "Invalid"),
    ("0345453747", "Invalid"),
    ("9780316066525", "Valid"),
    ("9780345453747", "Valid"),
    ("9783866155237", "Valid"),
    ("9783876155237", "Invalid"),
    ("0316066524", "9780316066525"),
    ("3866155239", "9783866155237"),
    ("817450494X", "9788174504944"),
    ("1", "Invalid"),
    ("123", "Invalid"),
]


@pytest.mark.parametrize("candidate, expected", test_cases)
def test_isbn_validation(candidate, expected):
    """Test isbn validation"""
    assert validate_isbn(candidate) == expected
