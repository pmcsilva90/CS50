#include <stdio.h>

int main(argc, argv[])
{

    if(argc != 2)
    {
        printf("Usage: ./caesar key\n");
        main = 1;
    }
    else if(argv[1] <= '0' || argv[1] >= '9')
    {
        printf("Usage: ./caesar key\n")
    }
}
