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
        
    }
}

int count_words(string text)
{
    // Return the number of words in text
}

int count_sentences(string text)
{
    // Return the number of sentences in text
}