import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) (to|-) (\d{1,2}):?(\d{2})? (AM|PM)", s)
    print(matches.groups())

    for n in range(1, len(matches.groups()) + 1):
        print(matches.group(n), type(matches.group(n)))

    if matches.group(2) == None:
        print("just None works")

    return "done"


if __name__ == "__main__":
    main()
