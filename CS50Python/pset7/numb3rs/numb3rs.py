import re
import sys


def main():
    #print(validate(input("IPv4 Address: ")))
    validate(input("IPv4 Address: "))

def validate(ip):
    matches = re.search(r"^([0-9])\.([0-9])\.([0-9])\.([0-9])$", ip)
    for match in matches:
        print(matches.group(match))






if __name__ == "__main__":
    main()
