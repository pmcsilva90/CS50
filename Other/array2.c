#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n = get_int("Size of array2: ");

    int array2[n];

    for(int i = 0; i < n; i++)
    {
        array2[n] = array2[i];
        printf("%i\n", array2[n]);
    }

    printf("pos 4 is %i\n", array2[3]);

}
