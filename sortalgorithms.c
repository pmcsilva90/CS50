#include <stdio.h>
#include <cs50.h>
#include <strings.h>
#include <string.h>
#include <stdlib.h>

void bubbleSort(void);
void selectionSort(void);
void insertionSort(void);
void swap(int xp, int yp);

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
    for (int i = 0; i < lenght - 1; i++)
    {
        minIndex = i;
        for (int j = i + 1; j < lenght; j++)
        {
            if (array[j] < array[minIndex])
            {
                minIndex = j;
            }
        }
    }
}

void insertionSort(void)
{

}

void swap(int xp, int yp)
{
    int xp;
    int yp;
    int temp;

    temp = xp
    yp = xp
    xp = temp

}

