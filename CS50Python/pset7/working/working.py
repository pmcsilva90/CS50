import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) (to|-) (\d{1,2}):?(\d{2})? (AM|PM)", s):
        start_h, start_m, start_ampm, prep, end_h, end_m, end_ampm = matches.groups()

        # Check for valid start hour and convert
        start_h = int(start_h)
        if not 0 < start_h <= 12:
            raise ValueError("Invalid time")
        if start_ampm == "PM" and start_h < 12:
            start_h += 12
        elif start_ampm == "AM" and start_h == 12:
            start_h = 0

        # Check for valid end hour and convert
        end_h = int(end_h)
        if not 0 < end_h <= 12:
            raise ValueError("Invalid time")
        if end_ampm == "PM" and end_h < 12:
            end_h += 12
        elif end_ampm == "AM" and end_h == 12:
            end_h = 0

        # Check for invalid hour output
        if not (0 <= start_h < 24 and 0 <= end_h < 24):
            raise ValueError("Invalid time")

        # Check for valid start minutes
        if start_m:
            start_m = int(start_m)
            if not (0 <= start_m < 60):
                raise ValueError("Invalid time")
        else:
            start_m = 0

        # Check for valid end minutes
        if end_m:
            end_m = int(end_m)
            if not (0 <= end_m < 60):
                raise ValueError("Invalid time")
        else:
            end_m = 0

        # Check for correct format
        if not prep == "to":
            raise ValueError("Invalid format")

        return f"{start_h:02d}:{start_m:02d} to {end_h:02d}:{end_m:02d}"
    else:
        raise ValueError("Invalid format")



if __name__ == "__main__":
    main()
