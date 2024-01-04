#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>

bool valid_key(string argv[1]);

int main(int argc, string argv[])
{

    if(argc != 2)
    {
        printf("Usage: ./caesar key\n");
        int main = 1;
    }
    else if(&valid_key == 0)
    {
        printf("Usage: ./caesar key(digit)\n");
    }
}


bool valid_key(string argv[1])
{
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (isdigit(argv[1][i]) = 0);
        valid_key(argv[1]) = 0;
    }
}
