#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height;

    do
    {
        height = get_int("Height: ");
    }
    while(height > 8 || height < 1);

    for(int c = 0; c < height + 1; c++)
    {
        for(int r = 0; r < c; r++)
        {
            printf("#");
        }
        printf("\n");
    }



}
