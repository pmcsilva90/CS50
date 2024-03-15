import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
    # --> https://youtu.be/xvFZjo5PgG0
    # <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    # --> https://youtu.be/xvFZjo5PgG0
    # <iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>
    # --> None

    matches = re.search(r".+(youtube\.com/embed/.+)\".+", s, re.IGNORECASE)
    return matches.group(1)


if __name__ == "__main__":
    main()
