#include <stdio.h>
#include <cs50.h>

int main(int argc, string argv[])
{
    for (int i = 0; i < argc; i++)
    {
       printf("argv %c", i + 1, argv[i]);
    }
}
