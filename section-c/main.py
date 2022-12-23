"""integrated service for deta deployment"""
from fastapi import FastAPI


def isbn_multiplier(length, index):
    """Return the appropriate validation multiplier based on length"""
    assert length in (10, 13)
    if length == 10:
        return 10 - index

    return 1 if index % 2 == 0 else 3


def isbn_modulus(length):
    """Return the appropriate validation modulus based on length"""
    assert length in (10, 13)
    return 11 if length == 10 else 10


def is_valid_isbn(candidate: str) -> bool:
    """Determine whether the given isbn number passes it's validity checksum"""
    isbn_length = len(candidate)

    if isbn_length not in [10, 13]:
        return False

    # X is only valid for isbn-10 and only in the last position
    if -1 < candidate.find("X") < 9 and isbn_length == 10:
        return False

    # convert string to a list of integers
    digits = [
        # handle X for ISBN_10
        10 if digit == "X" else int(digit)
        for digit in candidate
    ]

    total = sum(
        (
            digit * isbn_multiplier(isbn_length, index)
            for index, digit in enumerate(digits)
        )
    )
    return total % isbn_modulus(isbn_length) == 0


def convert_isbn10(isbn10: str) -> str:
    """Convert an isbn-10 to an isbn-13"""
    possible_isbns = (f"978{isbn10[:-1]}{check_digit}" for check_digit in range(1, 9))

    for isbn13 in possible_isbns:
        if is_valid_isbn(isbn13):
            return isbn13

    return None  # pragma: no cover


def validate_isbn(candidate: str) -> str:
    """Validate an isbn-10 or isbn-13 number"""
    if not is_valid_isbn(candidate):
        return "Invalid"

    if len(candidate) == 10:
        isbn13 = convert_isbn10(candidate)
        if not isbn13:
            return "Invalid: isbn-10 conversion failed"  # pragma: no cover
        return isbn13

    return "Valid"


app = FastAPI()


@app.get("/isbn/{isbn}")
def read_isbn_validation(isbn: str):
    """Validate and convert to isbn13"""
    return {"result": validate_isbn(isbn)}
