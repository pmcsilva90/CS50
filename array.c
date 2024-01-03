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

    for(i = 0; i < lenght; i++)
    {
        



        printf("%i\n", array[i]);
        }
    }

}
