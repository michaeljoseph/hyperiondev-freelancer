import pytest

from eyesbeen import isbn_modulus, isbn_multiplier


def test_isbn_multiplier():
    assert isbn_multiplier(10, 1) == 9
    assert isbn_multiplier(13, 4) == 1
    assert isbn_multiplier(13, 5) == 3

    with pytest.raises(AssertionError):
        assert isbn_multiplier(20, 5) == 3


def test_isbn_modulus():
    assert isbn_modulus(10) == 11
    assert isbn_modulus(13) == 10

    with pytest.raises(AssertionError):
        assert isbn_modulus(15) == 10
