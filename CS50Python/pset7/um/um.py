import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    counter = 0
    #matches = re.findall(r"\W\s?(um|Um)[,\.\?!:;\s\n]", s)
    matches = re.findall(r"\W(um|Um)\W", s)

    for _ in matches:
        counter += 1

    return counter

if __name__ == "__main__":
    main()
