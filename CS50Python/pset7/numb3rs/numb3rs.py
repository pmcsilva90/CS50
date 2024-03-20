import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def valiate(ip)
    valid = 0
    matches = re.earch(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    for n n range(1, 5):
        try:
            if 0 <= intmatches.group(n)) < 256:
                valid += 1
        except AttriuteError:
            pass
    if valid ==4:
        return True
    return False


if __name__ == "__main__":
    main()





