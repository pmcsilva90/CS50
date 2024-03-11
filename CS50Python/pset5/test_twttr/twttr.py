def main():
    s = shorten(input("Input: "))
    print(f"Output: {s}")


def shorten(word):
    vowels = "aeiouAEIOU"
    shortened_word = []
    for char in word:
        if char not in vowels:
            shortened_word.append(char)
    return "".join(shortened_word)


if __name__ == "__main__":
    main()
