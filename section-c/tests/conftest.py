import pytest


@pytest.fixture
def invalid_isbn10s():
    return [
        ("031606652X", "Invalid"),
        ("0316X6652X", "Invalid"),
        ("0330301824", "Invalid"),
        ("0345453747", "Invalid"),
    ]


@pytest.fixture
def isbn_conversions():
    return [
        ("0316066524", "9780316066525"),
        ("3866155239", "9783866155237"),
        ("817450494X", "9788174504944"),
    ]


@pytest.fixture
def isbn13s():
    return [
        ("9780316066525", "Valid"),
        ("9780345453747", "Valid"),
        ("9783866155237", "Valid"),
        ("9783876155237", "Invalid"),
    ]
