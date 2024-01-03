#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int size;
    int array[size];

    scanf("%i", &size);

    for(i = 1, i <= size, i = i * 2)
    {
        printf("%i\n", array[i]);
    }
}
