// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>
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

// Keep track of word count
int word_count = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int hash_val = hash(word);
    node *cursor = table[hash_val];
    while (cursor->next != NULL)
    {
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
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

        int hash_val = hash(new_node->word);

        new_node->next = table[hash_val]->next;
        table[hash_val]->next = new_node;
        word_count++;
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
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO

    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        node *tmp = cursor;
        while (cursor->next != NULL)
        {
            cursor = cursor->next;
            free(tmp);
            tmp = cursor;
        }
    }
    return true;
}
