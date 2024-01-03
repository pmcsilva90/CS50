#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int size = 0;

    scanf("%i", &size);

    int array[size];

    for(int i = 1; i <= size; i++)
    {
        printf("%i\n", array[i]);
    }

}
