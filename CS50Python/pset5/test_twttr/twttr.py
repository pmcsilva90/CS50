def main():
    s = input("Input: ")
    shorten(s)
    print(f"Output: {s}")


def shorten(word):
    vowels = "aeoiuAEIOU"
    shortened_word = []
    for char in word:
        if char not in vowels:
            shortened_word.append(char)
    return ''.join(shortened_word)


if __name__ == "__main__":
    main()
