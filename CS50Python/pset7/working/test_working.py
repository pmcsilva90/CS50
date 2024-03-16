from working import convert

def test_case():
    assert convert("12:01 AM to 07:08 PM") == True
    assert convert("10:00 PM to 02:40 PM") == True
    assert convert("9 PM to 7 AM") == True
    assert convert("2 AM to 1 AM") == True

    assert convert("05:31 pm to 10:31 AM") == ValueError: Invalid format
    assert convert("02:35 AM to 09:30 am") == ValueError: Invalid format
    assert convert("09:48 Pm to 09:16 Am") == ValueError: Invalid format
    assert convert("06:29 aM to 12:51 AM") == ValueError: Invalid format
    assert convert("02 am to 10 AM") == ValueError: Invalid format
    assert convert("11 am to 4 am") == ValueError: Invalid format


def test_inrange():
    assert convert("08:30 PM to 12:43 AM") == True
    assert convert("07:31 PM to 11:26 AM") == True
    assert convert("10 AM to 4 PM") == True
    assert convert("10 PM to 12 PM") == True

    assert convert("11:82 AM to 07:47 AM") == "ValueError: Invalid time"
    assert convert("13:08 PM to 04:29 PM") == ValueError
    assert convert("-2:31 AM to 10:06 AM") == ValueError
    assert convert("04:53 PM to -6:57 AM") == ValueError
    assert convert("06:23 PM to 02:60 PM") == ValueError
    assert convert("08:41 PM to 24:15 PM") == ValueError
    assert convert("2 AM to 16 PM") == ValueError


def test_format():
    assert convert("02:56PM to 03:2 AM") == ValueError: Invalid format
    assert convert("7 AM - 5 AM") == ValueError: Invalid format
    assert convert("07:5 PM to 12:4 PM") == ValueError: Invalid format
    assert convert("8PM - 3PM") == ValueError: Invalid format
    assert convert("08:13 AM until 01:03 PM") == ValueError: Invalid format

if __name__ == "__main__":
    main()
