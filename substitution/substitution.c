#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    int count[26] = {0}; // Array to store count of each letter

    for (int i = 0; i < strlen(argv[1]); i++)
    {

        //check for letters only
        if (isalpha(argv[1][i]) == 0)
        {
            printf("Key must be letters only\n");
            return 1;
        }

        //check for 26 char
        else if (strlen(argv[1]) != 26)
        {
            printf("Key must be 26 letters\n");
            return 1;
        }

        // Convert the character to lowercase and calculate its index
        int index = tolower(argv[1][i]) - 'a';

        // Check if the letter has already appeared in the key
        if (count[index] > 0)
        {
            printf("Key must not repeat letters\n");
            return 1;
        }

        // Increment count for the letter
        count[index]++;
    }

    string plaintext = get_string("plaintext: ");

    printf("ciphertext: ");

    for (int i = 0; i < strlen(plaintext); i++)
    {
        plaintext[i] = argv[1][i];
        printf("%c", plaintext[i]);
    }
    printf("\n");
}


