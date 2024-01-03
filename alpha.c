#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string word = get_string("Word: ");
    int i;
    int inOrder;


    for(i = 0; i < strlen(word); i++)
    {
        if(word[i] < word[i + 1])
        {
            inOrder++;
        }

    if(inOrder == strlen(word))
    {
        printf("True");
    }
    else
    {
        printf("False");
    }

}
