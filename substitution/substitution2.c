#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

bool isInvalidKey(const char *key) {
    int length = strlen(key);

    // Check if the string length is not equal to 26
    if (length != 26) {
        return true;
    }

    int count[26] = {0}; // Array to store count of each letter

    for (int i = 0; i < length; i++) {
        // Check if the character is not an alphabetic character
        if (!isalpha(key[i])) {
            return true;
        }

        // Convert the character to lowercase and calculate its index
        int index = tolower(key[i]) - 'a';

        // Check if the letter has already appeared in the key
        if (count[index] > 0) {
            return true;
        }

        // Increment count for the letter
        count[index]++;
    }

    // Check if all letters appeared exactly once
    for (int i = 0; i < 26; i++) {
        if (count[i] != 1) {
            return true;
        }
    }

    return false; // Key is valid
}

int main(int argc, char *argv[]) {
    // Check the number of command-line arguments
    if (argc != 2) {
        printf("Usage: %s key\n", argv[0]);
        return 1;
    }

    // Check if the key is invalid
    if (isInvalidKey(argv[1])) {
        printf("Invalid key.\n");
        return 1;
    }

    char plaintext[1000];
    printf("plaintext: ");
    fgets(plaintext, sizeof(plaintext), stdin);

    printf("ciphertext: ");
    for (size_t i = 0; i < strlen(plaintext); i++) {
        if (isalpha(plaintext[i])) {
            char plainChar = islower(plaintext[i]) ? 'a' : 'A';
            int index = tolower(plaintext[i]) - 'a';
            char cipherChar = argv[1][index];
            printf("%c", islower(plaintext[i]) ? tolower(cipherChar) : toupper(cipherChar));
        } else {
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");

    return 0;
}
