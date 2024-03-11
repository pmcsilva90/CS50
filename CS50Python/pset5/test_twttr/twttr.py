def main():
    s = input("Input: ")
    shorten(s)
    print(f"Output: {s}")


def shorten(word):
    for c in word:
        if c.lower() in ['a', 'e', 'i', 'o', 'u']:
            print(c, end="")
        else:
            print(c, end="")


if __name__ == "__main__":
    main()
