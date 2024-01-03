#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int lenght;
    do
    {
        lenght = get_int("Length: ");
    }
    while (lenght < 1);

    int i;
    int array[lenght];
    array[0] = 1;
    printf("%i\n", array[0]);

    for(i = 1; i < lenght; i++)
    {
        array[i] = array[i - 1] * 2;
        printf("%i\n", array[i]);
    }
}
