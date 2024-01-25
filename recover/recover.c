#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{


    // First 3 bytes of JPEGs are 0xff 0xd8 0xff
    // 4th byte is either 0xe0, 0xe1, 0xe2, 0xe3, 0xe4, 0xe5, 0xe6, 0xe7, 0xe8, 0xe9, 0xea, 0xeb, 0xec, 0xed, 0xee, or 0xef
    // Put another way, the fourth byte’s first four bits are 1110.
    // FAT file system “block size” is 512 bytes (B)
    // 50 JPEGs total
    

}
