import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    valid = 0
    matches = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    for n in range(1, 5):
        try:
            if 0 <= int(matches.group(n)) < 256:
                valid += 1
        except AttributeError:
            pass
    if valid == 4:
        return True
    return False


if __name__ == "__main__":
    main()
