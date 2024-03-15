import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) (to|-) (\d{1,2}):?(\d{2})? (AM|PM)", s)
    print(matches.groups())

    start_h = matches.groups(1)
    start_m = matches.groups(2)
    start_ampm = matches.groups(3)
    

    return "done"


if __name__ == "__main__":
    main()
