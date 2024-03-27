#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string word = get_string("Word: ");
    int i;
    int inOrder = 0;


    for(i = 0; i < strlen(word); i++)
    {
        if(word[i] <= word[i + 1])
        {
            inOrder++;
        }
        /*else
        {
            inOrder = inOrder + 0;
        }*/
    }
    if(inOrder == strlen(word) - 1)
    {
        printf("True");
    }
    else
    {
        printf("False");
    }

}
