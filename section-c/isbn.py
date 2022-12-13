"""
https://edabit.com/challenge/C5mooK3wfdhoooeLw

# International Standard Book Numbers

The International Standard Book Number (ISBN) is a unique identifying number
given to each published book.

ISBNs assigned after January 2007 are 13 digits long (ISBN-13),
however books with 10-digit ISBNs are still in wide use.

## ISBN-10

An ISBN-10 is verified this way:
isbn10 = "0330301624"
Line up the digits with the numbers 10 to 1:
0	3	3	0	3	0	1	6	2	4
10	9	8	7	6	5	4	3	2	1
0   1   2   3   4   5   6   7   8   9 (index)

Multiply each digit with the number below it
(the 10th digit in an ISBN can be an X.  This last X simply means 10).

Sum up the products:
0 + 27 + 24 + 0 + 18 + 0 + 4 + 18 + 4 + 4 = 99

If the sum is divisible by 11, the ISBN-10 is valid.

## ASBN-13

An ISBN-13 is verified this way:
isbn13 = "9780316066525"
Line up the digits with alternating 1s and 3s:
9	7	8	0	3	1	6	0	6	6	5	2	5
1	3	1	3	1	3	1	3	1	3	1	3	1
0   1   2   3   4   5   6   7   8   9  10  11   12 (index)

Multiply each digit with the number below it and get the sum:
9 + 21 + 8 + 0 + 3 + 3 + 6 + 0 + 6 + 18 + 5 + 6 + 5 = 90

If the sum is divisible by 10, the ISBN-13 is valid.

## ISBN Conversion

Convert a valid ISBN-10 to ISBN-13 by tacking 978 to the start,
then changing the last digit (the check digit)
so that the resulting number passes the ISBN-13 check.

## Problem Statement

Create a function that takes a string of numbers (possibly with an X at the end) and...

- Return "Invalid" if it is not a valid ISBN-10 or ISBN-13.
- Return "Valid" if it is a valid ISBN-13.
- If it is a valid ISBN-10, convert it into an ISBN-13 and return the ISBN-13 number.
"""
import pytest

ISBN_10_MULTIPLIER = lambda index: 10 - index
ISBN_13_MULTIPLIER = lambda index: 1 if index % 2 == 0 else 3


class InvalidIsbn(Exception):
    pass


def is_valid_isbn(candidate: str) -> bool:
    isbn_length = len(candidate)

    # (multiplier, modulus)
    multiplier = ISBN_10_MULTIPLIER if isbn_length == 10 else ISBN_13_MULTIPLIER
    modulus = 11 if isbn_length == 10 else 10

    # X is only valid for isbn-10 and only in the last position
    if -1 < candidate.find("X") < 9 and isbn_length == 10:
        return False
        # raise InvalidIsbn(f"X is only valid for ISBN-10 and only in the last position ({candidate})")

    # convert string to a list of integers
    digits = [
        # handle X for ISBN_10
        10 if digit == "X" else int(digit)
        for digit in candidate
    ]

    total = sum([
        digit * multiplier(index)
        for index, digit in enumerate(digits)
    ])

    return total % modulus == 0


def convert_isbn10(isbn10: str) -> str:
    isbn13 = f"978{isbn10}"
    isbn12 = isbn13[:-1]
    for check_digit in range(1, 9):
        isbn13 = f"{isbn12}{check_digit}"
        if is_valid_isbn(isbn13):
            return isbn13

    raise IsbnException(f"Conversion failed: validating check digit not found for {isbn13}")


def isbn(candidate: str):
    """Validate an isbn-10 or isbn-13 number"""
    if len(candidate) == 13:
        return "Valid" if is_valid_isbn(candidate) else "Invalid"
    elif len(candidate) == 10:
        if is_valid_isbn(candidate):
            return convert_isbn10(candidate)
        else:
            return "Invalid"
    else:
        return "Invalid"


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

    ("1", "Invalid")
]


@pytest.mark.parametrize("candidate, expected", test_cases)
def test_isbn_validation(candidate, expected):
    assert isbn(candidate) == expected