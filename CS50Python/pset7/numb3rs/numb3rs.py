import re
import sys


def main():
    #print(validate(input("IPv4 Address: ")))
    validate(input("IPv4 Address: "))

def validate(ip):
    valid = True
    matches = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip)
    for n in range(4):
        if 0 < int(matches.group(n)) < 256:
            








if __name__ == "__main__":
    main()
