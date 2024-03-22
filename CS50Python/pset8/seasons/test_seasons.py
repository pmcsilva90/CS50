import seasons
import pytest
from datetime import date

def main():
    test_dateformat()
    test_invalid_date()
    test_valid_date()
    test_main()


def test_dateformat():
    with pytest.raises(SystemExit):
        assert seasons.validate_dob("19-03-1999") == "Invalid date"
    with pytest.raises(SystemExit):
        assert seasons.validate_dob("1-1-2001") == "Invalid date"
    with pytest.raises(SystemExit):
        assert seasons.validate_dob("10-5-2000") == "Invalid date"
    with pytest.raises(SystemExit):
        assert seasons.validate_dob("5-25-1998") == "Invalid date"
    with pytest.raises(SystemExit):
        assert seasons.validate_dob("18 03 1990") == "Invalid date"
    with pytest.raises(SystemExit):
        assert seasons.validate_dob("1994 06 08") == "Invalid date"
    with pytest.raises(SystemExit):
        assert seasons.validate_dob("1983, 11, 17") == "Invalid date"
    with pytest.raises(SystemExit):
        assert seasons.validate_dob("July 4th 1984") == "Invalid date"


def test_valid_date():
    assert seasons.validate_dob("2001-02-25") == date(2001, 2, 25)
    assert seasons.validate_dob("1990-03-17") == date(1990, 3, 17)
    assert seasons.validate_dob("1961-06-26") == date(1961, 6, 26)
    assert seasons.validate_dob("1980-02-01") == date(1980, 2, 1)


def test_invalid_date():
    with pytest.raises(SystemExit):
        assert seasons.validate_dob("1995-02-30") == "Invalid date"
    with pytest.raises(SystemExit):
        assert seasons.validate_dob("1974-13-25") == "Invalid date"
    with pytest.raises(SystemExit):
        assert seasons.validate_dob("1997-04-31") == "Invalid date"
    with pytest.raises(SystemExit):
        assert seasons.validate_dob("1945-07-32") == "Invalid date"
    with pytest.raises(SystemExit):
        assert seasons.validate_dob("999-01-02") == "Invalid date"

def test_main():
    with pytest.raises(SystemExit):
        assert seasons.main("random string") == "Invalid date"
    with pytest.raises(SystemExit):
        assert seasons.validate_dob("L3375p34k") == "Invalid date"
    with pytest.raises(SystemExit):
        assert seasons.validate_dob("2000BC-01-01") == "Invalid date"
    assert seasons.main()




