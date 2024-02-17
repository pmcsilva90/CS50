#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    // Check for command line args
    if (argc != 2)
    {
        printf("Usage: ./read infile\n");
        return 1;
    }

    // Create buffer to read into
    char buffer[7];

    // Create array to store plate numbers
    char *plates[8];

    FILE *infile = fopen(argv[1], "r");

    int idx = 0;

    while (fread(buffer, 1, 7, infile) == 7)
    {
        // Replace '\n' with '\0'
        buffer[6] = '\0';

        // Allocate memory for each plate number and copy contents
        plates[idx] = malloc(strlen(buffer) + 1);
        strcpy(plates[idx], buffer);
        idx++;
    }

    fclose(infile);

    // Print the plate numbers
    for (int i = 0; i < idx; i++)
    {
        printf("%s\n", plates[i]);

        // Free allocated memory
        free(plates[i]);
    }

    return 0;
}
