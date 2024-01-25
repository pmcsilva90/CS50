#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    // First 3 bytes of JPEGs are 0xff 0xd8 0xff
    // 4th byte is either 0xe0, 0xe1, 0xe2, 0xe3, 0xe4, 0xe5, 0xe6, 0xe7, 0xe8, 0xe9, 0xea, 0xeb, 0xec, 0xed, 0xee, or 0xef
    // Put another way, the fourth byte’s first four bits are 1110.
    // FAT file system “block size” is 512 bytes (B)
    // 50 JPEGs total

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
    uint8_t *buffer = malloc(sizeof(uint8_t) * 512);
    if (buffer == NULL)
    {
        printf("Could not allocate memory for buffer");
        return 1;
    }
    // Create string for file name
    char filename[8];
    // Create counter for found JPEGs
    int counter = 0;
    // Create pointer to output file
    FILE *output = NULL;

    // While there's still data left to read from the memory card
    while (fread(buffer, 1, 512, card) == 512)
    {
        // Create JPEGs from the data
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // If not first JPEG found, close previous one
            if (counter > 0)
            {
                fclose(output);
            }
            // Update filename to match counter
            sprintf(filename, "%03i.jpg", counter);
            // Create new file with filename
            output = fopen(filename, "w");
            // If pointing to invalid memory space, print error, close created file and exit program
            if (output == NULL)
            {
                printf("Could not create file\n");
                fclose(output);
                fclose(card);
                return 1;
            }
            // Update counter of found JPEGs
            counter++;
        }
        //Copy data from buffer to output file
        fwrite(buffer, 1, 512, output); ////////////////
    }
    // Close remaining files
    fclose(card);
    fclose(output);
    return 0;
}
