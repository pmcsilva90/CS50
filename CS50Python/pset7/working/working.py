import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"(\d{1,2}):?(\d{1,2}?) (to|-) (\d{1,2}):?(\d{1,2}?)")
    for n in range(1,4):
        print(matches.group(n))


if __name__ == "__main__":
    main()
