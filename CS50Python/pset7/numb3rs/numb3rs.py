import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^([0-9])\.([0-9])\.([0-9])\.([0-9])$", ip)
    print(matches.group())






if __name__ == "__main__":
    main()
