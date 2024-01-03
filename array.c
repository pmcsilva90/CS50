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


    for(i = 0; i < lenght; i++)
    {
        array[0] = i + 1;
        if (array[0] > 1)
        {
            array[i] = array[i - 1] * 2;
            printf("%i\n", array[i]);
        }
        else
        {
        printf("%i\n", array[i]);
        }
    }

}
