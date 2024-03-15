import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) (to|-) (\d{1,2}):?(\d{2})? (AM|PM)", s)
    print(matches.groups())
    valid_time = False

    if (0 < int(matches.group(1)) <= 12) and (0 < int(matches.group(5)) <= 12):
        if matches.group(2) and matches.group(6):
            if (0 <= int(matches.group(1)) < 60) and (0 <= int(matches.group(1)) < 60):
                valid_time = True



if __name__ == "__main__":
    main()
