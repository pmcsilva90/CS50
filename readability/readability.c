#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // Prompt user for text
    string text = get_string("Text: ");

    // Count number of letters, words, and sentences in text
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    // Compute the Coleman-Liau index
    float CLindex;
    float L;
    float S;

    L = letters * 100.0 / words;
    S = sentences * 100.0 / words;
    CLindex = 0.0588 * L - 0.296 * S - 15.8;

    // Print the grade level
    if (CLindex >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (CLindex < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %d\n", (int) round(CLindex));
    }

    // Testing
    /* printf("\n");
    printf("letters: %d\n", letters);
    printf("words: %d\n", words);
    printf("sentences: %d\n", sentences);
    printf("L: %f\n", L);
    printf("S: %f\n", S);
    printf("CLindex: %f\n", CLindex); */
}

int count_letters(string text)
{
    // Return the number of letters in text
    int l = 0;

    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            l += 1;
        }
        else
        {
            l += 0;
        }
    }
    return l;
}

int count_words(string text)
{
    // Return the number of words in text
    int w = 0;

    for (int i = 0; i < strlen(text); i++)
    {
        if (isspace(text[i]))
        {
            w += 1;
        }
        else
        {
            w += 0;
        }
    }
    return w + 1;
}

int count_sentences(string text)
{
    // Return the number of sentences in text
    int s = 0;

    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            s += 1;
        }
        else
        {
            s += 0;
        }
    }
    return s;
}
