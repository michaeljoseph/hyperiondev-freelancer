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

def is_valid_isbn10(candidate: str, multiplier) -> bool:
    # initialise digit sum counter
    total = 0

    # loop through the isbn digits
    for index, digit in enumerate(candidate):
        # handle trailing X digit
        if digit == 'X':
            if index != 9:
                return False

            digit = '10'

        # digit is a string, so convert to a number before multplying
        total += int(digit) * multiplier(index)

    # valid if cleanly divisible by 10
    return total % 11 == 0



def is_valid_isbn13(candidate: str, multiplier) -> bool:
    # initialise digit sum counter
    total = 0

    # loop through the isbn digits
    for index, digit in enumerate(candidate):
        # digit is a string, so convert to a number before multplying
        total += int(digit) * multiplier(index)

    # valid if cleanly divisible by 10
    return total % 10 == 0


def isbn(candidate: str):
    """Validate an isbn-10 or isbn-13 number"""
    if len(candidate) == 13:
        # the multiplier alternates between 1 and 3
        multiplier = lambda index: 1 if index % 2 == 0 else 3

        return "Valid" if is_valid_isbn13(candidate, multiplier) else "Invalid"
    elif len(candidate) == 10:
        # the multiplier starts at 9 and decreases
        multiplier = lambda index: 10 - index

        return "Valid" if is_valid_isbn10(candidate, multiplier) else "Invalid"
    else:
        raise Exception(f'Unexpected isbn length {len(candidate)}')



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
]


@pytest.mark.parametrize("candidate, expected", test_cases)
def test_isbn_validation(candidate, expected):
    assert isbn(candidate) == expected