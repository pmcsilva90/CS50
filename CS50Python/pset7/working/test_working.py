import pytest
from working import convert

def test_case():
    assert convert("12:01 AM to 07:08 PM") == "00:01 to 19:08"
    assert convert("10:00 PM to 02:40 PM") == "22:00 to 14:40"
    assert convert("9 PM to 7 AM") == "21:00 to 07:00"
    assert convert("2 AM to 1 AM") == "02:00 to 01:00"

    with pytest.raises(ValueError, match="Invalid format"):
        convert("05:31 pm to 10:31 AM")

    with pytest.raises(ValueError, match="Invalid format"):
        convert("02:35 AM to 09:30 am")

    with pytest.raises(ValueError, match="Invalid format"):
        convert("09:48 Pm to 09:16 Am")

    with pytest.raises(ValueError, match="Invalid format"):
        convert("06:29 aM to 12:51 AM")

    with pytest.raises(ValueError, match="Invalid format"):
        convert("02 am to 10 AM")

    with pytest.raises(ValueError, match="Invalid format"):
        convert("11 am to 4 am")


def test_inrange():
    assert convert("08:30 PM to 12:43 AM") == "20:30 to 00:43"
    assert convert("07:31 PM to 11:26 AM") == "19:31 to 11:26"
    assert convert("10 AM to 4 PM") == "10:00 to 16:00"
    assert convert("10 PM to 12 PM") == "22:00 to 12:00"

    with pytest.raises(ValueError, match="Invalid time"):
        convert("11:82 AM to 07:47 AM")

    with pytest.raises(ValueError, match="Invalid time"):
        convert("13:08 PM to 04:29 PM")

    with pytest.raises(ValueError, match="Invalid time"):
        convert("-2:31 AM to 10:06 AM")

    with pytest.raises(ValueError, match="Invalid time"):
        convert("04:53 PM to -6:57 AM")

    with pytest.raises(ValueError, match="Invalid time"):
        convert("06:23 PM to 02:60 PM")

    with pytest.raises(ValueError, match="Invalid time"):
        convert("08:41 PM to 24:15 PM")

    with pytest.raises(ValueError, match="Invalid time"):
        convert("2 AM to 16 PM")


def test_format():
    with pytest.raises(ValueError, match="Invalid format"):
        convert("02:56PM to 03:2 AM")

    with pytest.raises(ValueError, match="Invalid format"):
        convert("7 AM - 5 AM")

    with pytest.raises(ValueError, match="Invalid format"):
        convert("07:5 PM to 12:4 PM")

    with pytest.raises(ValueError, match="Invalid format"):
        convert("8PM - 3PM")

    with pytest.raises(ValueError, match="Invalid format"):
        convert("08:13 AM until 01:03 PM")
