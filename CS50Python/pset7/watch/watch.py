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

    matches = re.search(r".+(youtube\.com/embed/\w+).+", s, re.IGNORECASE)
    url = matches.group(1)
    url = "https://" + url.replace("youtube.com/embed", "youtu.be")

    try:
        return url
    except AttributeError:
        sys.exit("None")


if __name__ == "__main__":
    main()
