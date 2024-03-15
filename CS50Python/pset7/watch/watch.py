import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r".+(youtube\.com/embed/\w+).+", s, re.IGNORECASE)
    try:
        url = matches.group(1)
        url = "https://" + url.replace("youtube.com/embed", "youtu.be")
        return url
    except AttributeError:
        sys.exit("None")


if __name__ == "__main__":
    main()
