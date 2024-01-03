#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string word = get_string("Word: ");

    int i = 0;
    /*for(i = 0; i < strlen(word); i++)
    {
        word[i] = ("%i", word[i]);
    }*/
    for(i = 0; word[i] > 96)
    {
        if (word[i] > word[i + 1])
        {
        printf("False");
        }
        else
        printf("True");
    }
}
