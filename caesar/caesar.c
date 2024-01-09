#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char rotate(char c, int n);

int main(int argc, string argv[])
{
    // Check for exactly one command-line argument
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    // Check that every character in argument is digit
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (isdigit(argv[1][i]) == 0)
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }
    // printf("valid key!\n");
    // convert argument from string to int
    int key = atoi(argv[1]);

    // printf("key is %i\n", key);
    // prompt user for plaintext
    string plaintext = get_string("Plaintext: ");
    // print ciphertext
    printf("ciphertext: ");

    for (int i = 0; i < strlen(plaintext); i++)
    {
        printf("%c", rotate(plaintext[i], key));
    }
    printf("\n");
}

char rotate(char c, int n)
{
    if (c >= 'a' && c <= 'z')
    {
        c = 'a' + ((c - 'a' + n) % 26);
    }
    else if (c >= 'A' && c <= 'Z')
    {
        c = 'A' + ((c - 'A' + n) % 26);
    }
    return c;
}
