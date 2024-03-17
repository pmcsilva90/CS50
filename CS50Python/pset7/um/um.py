import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    counter = 0
    matches = re.findall(r"\s?(um|Um)[,\.\?!:;\s\n]", s)
    for _ in matches:
        counter += 1

    return counter

if __name__ == "__main__":
    main()
