from cs50 import get_string

def main():

    text = get_string("Text: ")

    count_words = 0
    count_letters = 0
    count_sentences = 0

    words = text.split(" ")
    for word in words:
        count_words += 1

    for char in text:
        if (c.isalpha()):
            count_letters += 1

    for char in text:
        if char in ['.', '!', '?']:
            count_sentences += 1




def L(text):


def S(text):

