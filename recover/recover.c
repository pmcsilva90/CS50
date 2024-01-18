#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>


int main(int argc, char *argv[])
{
// Accept a single command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open the memory card
    FILE *card = fopen(argv[1], "r");

    if (card == NULL)
    {
        printf("Could not open file\n");
        return 1;
    }

    // Create a buffer for a block of data
    uint8_t buffer[512];
    uint8_t BYTE1, BYTE2, BYTE3, BYTE4;
    char jpeg[3];

    

    // While there's still data left to read from the memory card
    while (fread(buffer, 1, 512, card) == 512)
    {
        // Create JPEGs from the data
        // Open output file
        FILE *jpeg = fopen(outfile, "w");
        if (outptr == NULL)
        {
            fclose(inptr);
            printf("Could not create %s.\n", outfile);
            return 1;
    }
    }
}
