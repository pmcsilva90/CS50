#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while(height < 1 || height > 8);

    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < height; col++)
        {
            printf("#");
        }
        printf("\n");
    }
}
