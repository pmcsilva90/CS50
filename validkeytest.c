#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include <cs50.h>

bool isInvalidKey(const char *key)
{
    int length = strlen(key);

    // Check if the string length is not equal to 26
    if (length != 26)
    {
        return true;
    }

    int count[26] = {0}; // Array to store count of each letter

    for (int i = 0; i < length; i++)
    {
        // Check if the character is not an alphabetic character
        if (!isalpha(key[i]))
        {
            return true;
        }

        // Convert the character to lowercase and calculate its index
        int index = tolower(key[i]) - 'a';

        // Check if the letter has already appeared in the key
        if (count[index] > 0)
        {
            return true;
        }

        // Increment count for the letter
        count[index]++;
    }

    // Check if all letters appeared exactly once
    for (int i = 0; i < 26; i++)
    {
        if (count[i] != 1)
        {
            return true;
        }
    }

    return false; // Key is valid
}

int main() {
    const char *validKey = "AbCdEfGhIjKlMnOpQrStUvWxYz"; // Example valid key (case insensitive)
    const char *invalidKey = "aBcDeFgHiJkLmNoPqRsTuVwXyZz"; // Example invalid key (case insensitive)
    string key = get_string("key: ");

    if (isInvalidKey(key))
    {
        printf("The key is invalid.\n");
    }
    else
    {
        printf("The key is valid.\n");
    }

    /*if (isInvalidKey(invalidKey)) {
        printf("The key is invalid.\n");
    } else {
        printf("The key is valid.\n");
    }*/

    return 0;
}
