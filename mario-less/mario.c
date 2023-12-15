#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Ask user for height between 1 and 8
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while(height < 1 || height > 8);

    // Make right aligned pyramid
    for (int row = 0; row < height; row++)
    {
        for (int space = 0; space < height - row - 1; space++)
        {
            printf(" ");
        }
        for (int column = 0; column <= row; column++)
        {
            printf("#");
        }
        printf("\n");
    }
}
