import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r"*\s(um|Um)", s)

# Hello. Um,

...


if __name__ == "__main__":
    main()
