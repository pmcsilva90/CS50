import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) (to|-) (\d{1,2}):?(\d{2})? (AM|PM)", s)
    print(matches.groups())
    valid_time = False

    start_h = int(str(matches.groups(1)))
    start_m = int(str(matches.groups(2)))
    start_ampm = str(matches.groups(3))
    to = str(matches.groups(4))
    end_h = int(str(matches.groups(5)))
    end_m = int(str(matches.groups(6)))
    end_ampm = str(matches.groups(7))

    if (0 < start_h < 13) and (0 < end_h < 13) and (0 <= start_m < 60) and (0 <= end_m < 60):
        valid_time = True
    if to != "to":
        sys.exit("to error")
    if start_ampm == "PM":
        start_h += 12
    if end_ampm == "PM":
        end_h += 12

    if valid_time:
        return f"{start_h}:{start_m} to {end_h}:{end_m}"


if __name__ == "__main__":
    main()
