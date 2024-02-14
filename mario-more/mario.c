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

    for(int c = 0; c < height; c++)
    {

        for(int s = 0; s < height - 1 - c; s++)
        {
            printf(" ");
        }
        for(int r = 0; r <= c; r++)
        {
            printf("#");
        }
        printf("  ");
        for(int r = 0; r <= c; r++)
        {
            printf("#");
        }
        printf("\n");
    }



}
