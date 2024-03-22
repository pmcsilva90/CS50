import seasons
import pytest

def main():
    test_dateformat()
    test_valid_date()


def test_dateformat():
    assert seasons.validate_dob("10-02-1999") == ValueError
    # assert validate_dob("") ==
    # assert validate_dob("") ==
    # assert validate_dob("") ==
