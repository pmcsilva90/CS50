#include <stdio.h>
#include <cs50.h>
#include <strings.h>
#include <string.h>
#include <stdlib.h>

void bubbleSort(void);
void selectionSort(void);
void insertionSort(void);

int main(int argc, string argv[])
{
    int array[];
    int lenght = 10;

    for (int i = 0; i < lenght; i++)
    {
        array[i] = get_int("Element %i: ", i + 1);
        printf("\n");
    }

    for (int i = 0; i < lenght; i++)
    {
        printf("Element %i is %i", i + 1, array[i])
    }


    if (argc == 1)
    {
        get_string ("Sorting Algorithm: ")
    }
    else if (strcasecmp(argv[1], "selection"))
}

void bubbleSort(void)
{

}

void selectionSort(void)
{

}
