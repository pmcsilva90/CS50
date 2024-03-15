import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))
    #validate(input("IPv4 Address: "))

def validate(ip):
    valid = 0
    matches = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip)
    for n in range(4):
        if 0 < int(matches.group(n)) < 256:
            valid += 1
    if valid == 4:
        return True
    return False


if __name__ == "__main__":
    main()
