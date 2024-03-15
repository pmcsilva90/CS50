import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) (to|-) (\d{1,2}):?(\d{2})? (AM|PM)", s)
    print(matches.groups())
    valid_time = False
    start_h = int(matches.group(1))
    start_m = int(matches.group(2))
    start_ampm = matches.group(3)
    to = matches.group(4)
    end_h = int(matches.group(5))
    end_m = int(matches.group(6))
    end_ampm = matches.group(7)

    if (0 < start_h <= 12) and (0 < end_h <= 12):
        if (0 <= start_m < 60) and (0 <= end_m < 60):
            valid_time = True
    if start_ampm == "PM":
        start_h += 12
    if end_ampm == "PM":
        end_h += 12
    if to != "to":
        sys.exit("to error")

    return f"{}{}{}{}"




if __name__ == "__main__":
    main()
