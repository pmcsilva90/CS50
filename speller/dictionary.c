// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int i = 0;

    while (isalpha(word[i]) == 0)
    {
        i++;
    }
    return toupper(word[i]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    // Open the dictionary file
    FILE *source = fopen(dictionary, "r");
    if (source == NULL)
    {
        printf("Could not open dictionary %s\n", dictionary);
        fclose(source);
        return false;
    }

    // Read each word in the file
    char *buffer = malloc(sizeof(char) * (LENGTH + 1));
    if (buffer == NULL)
    {
        printf("Could not allocate memory for buffer\n");
        return false;
    }
    while (fscanf(source, "%s", buffer) != EOF)
    {
        // Add each word to the hash table
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            printf("Could not allocate memory for new node %s\n", buffer);
            return false;
        }
        strcpy(new_node->word, buffer);
        new_node->next = NULL;

        int hash_num = hash(new_node->word);

        new_node->next = table[hash_num]->next;
        table[hash_num]->next = new_node;
    }

    // Close the dictionary file
    fclose(source);
    free(buffer);

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
