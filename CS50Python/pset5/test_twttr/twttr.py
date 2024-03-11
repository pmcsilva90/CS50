def main():
    s = input("Input: ")
    shorten(s)
    print(f"Output: {s}")


def shorten(word):
    vowels = "aeoiu"
    shortened_word = []
    for char in word:
        if char.lower() not in vowels:
            shortened_word.append(char)
    return shortened_word


if __name__ == "__main__":
    main()