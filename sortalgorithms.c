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
    string algorithm;

    for (int i = 0; i < lenght; i++)
    {
        array[i] = get_int("Element %i: ", i + 1);
        printf("\n");
    }
    for (int i = 0; i < lenght; i++)
    {
        printf("Element %i is %i", i + 1, array[i]);
    }


    if (argc == 1)
    {
        printf("Choose one of the sorting algorithms: bubble, selection or sort")
        algorithm = get_string ("Sorting Algorithm: ")
        if (strcasecmp(algorithm, "selection" == 0))
        {
            selectionSort();
        }
        else if (strcasecmp(algorithm, "bubble" == 0))
        {
            bubbleSort();
        }
        else if (strcasecmp(algorithm, "insertion" == 0))
        {
            insertionSort();
        }
        else
        {
            printf("Algorithm invalid\n")
            return 1;
        }
        printf("\n\n")
    }
    else if (strcasecmp(argv[1], "selection" == 0))
    {
        selectionSort();
    }
    else if (strcasecmp(argv[1], "bubble" == 0))
    {
        bubbleSort();
    }
    else if (strcasecmp(argv[1], "insertion" == 0))
    {
        insertionSort();
    }
    else
    {
        printf("Usage: %s algorithm", argv[0])
        return 2;
    }

    printf("Sorted array\n");

    for (int i = 0; i < lenght; i++)
    {
        printf("%i", array[i]);
    }

    return 0;
}

void swap(int xp, int yp)
{
    int temp;

    temp = xp;
    xp = yp;
    yp = temp;

}

void bubbleSort(void)
{

}

void selectionSort(void)
{
    for (int i = 0; i < lenght - 1; i++)
    {
        int minIndex = i;
        for (int j = i + 1; j < lenght; j++)
        {
            if (array[j] < array[minIndex])
            {
                minIndex = j;
            }
        }
        if (minIndex != i)
        {
            swap(array[minIndex], array[i])
        }
    }
}

void insertionSort(void)
{

}



