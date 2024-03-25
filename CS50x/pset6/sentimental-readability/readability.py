from cs50 import get_string

def main():

    text = get_string("Text: ")

    words = count_words(text)
    letters = count_letters(text)
    sentences = count_sentences(text)

    l = L(letters, words)
    s = S(sentences, words)

    grade = CLindex(l, s)

    if grade < 1:
        print("Before Grade 1")
    elif grade >= 16:
        print("Grade 16+")
    else:
        print(f"Grade: {grade:.0f}")

def count_words(text):

    count_words = 0
    words = text.split(" ")
    for word in words:
        count_words += 1
    return count_words

def count_letters(text):

    count_letters = 0
    for char in text:
        if (char.isalpha()):
            count_letters += 1
    return count_letters

def count_sentences(text):

    count_sentences = 0
    for char in text:
        if char in ['.', '!', '?']:
            count_sentences += 1
    return count_sentences


def L(letters, words):
    return letters / words * 100

def S(sentences, words):
    return sentences / words * 100

def CLindex(L, S):
    return 0.0588 * L - 0.296 * S - 15.8

if __name__ == "__main__":
    main()

