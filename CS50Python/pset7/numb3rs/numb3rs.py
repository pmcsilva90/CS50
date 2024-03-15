import re
import sys


def main():
    #print(validate(input("IPv4 Address: ")))
    validate(input("IPv4 Address: "))

def validate(ip):
    #matches = re.search(r"^([0-9])\.([0-9])\.([0-9])\.([0-9])$", ip)
    lol = ip.split(".")
    for _ in lol:
        print(_)
    print(type(lol))






if __name__ == "__main__":
    main()
