import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) (to|-) (\d{1,2}):?(\d{2})? (AM|PM)", s):
        start_h, start_m, start_ampm, prep, end_h, end_m, end_ampm = matches.groups()






if __name__ == "__main__":
    main()
