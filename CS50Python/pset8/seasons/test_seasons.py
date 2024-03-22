import seasons
import pytest

def main():
    test_dateformat()
    test_valid_date()


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

    assert seasons.validate_dob("2001-02-25") == "2001-02-25"

