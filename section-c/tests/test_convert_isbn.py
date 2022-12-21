from eyesbeen import convert_isbn10


def test_convert_isbn10(isbn_conversions):
    for isbn10, isbn13 in isbn_conversions:
        assert convert_isbn10(isbn10) == isbn13
