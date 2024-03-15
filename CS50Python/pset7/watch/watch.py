import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"<iframe.+(youtube\.com/embed/\w+).+</iframe>", s, re.IGNORECASE):
        url = matches.group(1)
    else:
        return matches

    url = "https://" + url.replace("youtube.com/embed", "youtu.be")
    return url


if __name__ == "__main__":
    main()
