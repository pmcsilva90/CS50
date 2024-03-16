import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) (to|-) (\d{1,2}):?(\d{2})? (AM|PM)", s):
        start_h, start_m, start_ampm, prep, end_h, end_m, end_ampm = matches.groups()

        start_h = int(start_h)
        if start_ampm == "PM" and start_h < 12:
            start_h += 12
        elif start_ampm == "AM" and start_h == 12:
            start_h = 0

        end_h = int(end_h)
        if end_ampm == "PM" and end_h < 12:
            end_h += 12
        elif end_ampm == "AM" and end_h == 12:
            end_h = 0

        if not (0 <= start_h < 24 and 0 <= end_h < 24):
            raise ValueError("Invalid time")

        if start_m:
            if not (0 <= start_m < 60):
                raise ValueError("Invalid time")
        else:
            start_m = 0

        if end_m:
            if not (0 <= end_m < 60):
                raise ValueError("Invalid time")
        else:
            end_m = 0

        if not prep == "to":
            raise ValueError("Invalid format")

        return f"{start_h:}:{start_m} to {end_h}:{end_m}"
    else:
        raise ValueError("Invalid format")



if __name__ == "__main__":
    main()
