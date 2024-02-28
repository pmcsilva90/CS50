// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>

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

for (int i = 0; i < 26; i++)
{
    table[i]->word = 'A' + i;
    table[i]->next = NULL;
}

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
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    // Open the dictionary file
    FILE *source = fopen(dictionary, "r")
    if (source == NULL)
    {
        printf("Could not open dictionary");
        fclose(source);
        return false;
    }

    // Read each word in the file
    char *buffer = malloc(sizeof((LENGHT + 1) * char));
    if (buffer == NULL)
    {
        printf("Could not allocate memory for buffer");
        free(buffer);
        return false;
    }
    while (fscanf(source, "%s", buffer) != EOF)
    {
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            printf("Could not allocate memory for new node %s", buffer);
            free(new_node);
            return false;
        }
        new_node->word = sprintf(buffer, "%s");
        new_node->next = NULL;
        int hash_num = hash(new_node->word);
        table[hash_num]->next = new_node;
        

    }


        // Add each word to the hash table

    // Close the dictionary file
    fclose(source);
    free(buffer);

    return false;
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
