#include <ctype.h>
#include <cs50.h>
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

    // Print the grade level
}

int count_letters(string text)
{
    // Return the number of letters in text
    int l = 0;

    for (int i = 0; i < strlen(text); i++)
    {
        if(isaplha(text[i]))
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
        if(isspace(text[i]))
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
        if(text[i] == '.' || text[i] == '?' || text[i] == '!')
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
