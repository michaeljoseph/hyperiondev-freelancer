from eyesbeen import is_valid_isbn


def test_length_check():
    assert not is_valid_isbn("1")
    assert not is_valid_isbn("123")
    assert not is_valid_isbn("12345678901234")


def test_exes_in_isbn10s():
    assert not is_valid_isbn("0316X6652X")
    assert not is_valid_isbn("978031606652X")
