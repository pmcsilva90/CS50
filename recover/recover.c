#include <stdio.h>
#include <stdlib.h>

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
        printf("Could not open file");
        return 1;
    }

    // Create a buffer for a block of data
    uint8_t buffer[512];

    // While there's still data left to read from the memory card
    while (fread(buffer, 1, 512, card) == 512)
    {
        // Create JPEGs from the data

        fopen()
    }

}
