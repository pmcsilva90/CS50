from cs50 import get_string

def main():

    text = get_string("Text: ")

    words = count_words(text)
    letters = count_letters(text)
    sentences = count_sentences(text)

    l = L(letters, words)
    s = S(sentences, words)

    grade = CLindex(l, s)

    print(f"Grade: {grade:00d}")

def count_words(text):

    words = text.split(" ")
    for word in words:
        count_words += 1

def count_letters(text):

    for char in text:
        if (c.isalpha()):
            count_letters += 1

def count_sentences(text):

    for char in text:
        if char in ['.', '!', '?']:
            count_sentences += 1


def L(letters, words):
    return letters / words * 100

def S(sentences, words):
    return sentences / words * 100

def CLindex(L, S):
    return 0.0588 * L - 0.296 * S - 15.8

if __name__ == "__main__":
    main()

