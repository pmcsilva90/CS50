#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#define LENGHT 10

int array[LENGHT];

void bubbleSort(void);
void selectionSort(void);
void insertionSort(void);
void swap(int *xp, int *yp);

int main(int argc, string argv[])
{
    string algorithm;

    for (int i = 0; i < LENGHT; i++)
    {
        array[i] = get_int("Element %i: ", i + 1);
    }
    printf("\n");
    for (int i = 0; i < LENGHT; i++)
    {
        printf("Element %i is %i\n", i + 1, array[i]);
    }

    printf("\n");

    if (argc == 1)
    {
        printf("Choose one of the sorting algorithms: bubble, selection or sort\n");
        algorithm = get_string("Sorting Algorithm: ");
        if (strcasecmp(algorithm, "selection") == 0)
        {
            selectionSort();
        }
        else if (strcasecmp(algorithm, "bubble") == 0)
        {
            bubbleSort();
        }
        else if (strcasecmp(algorithm, "insertion") == 0)
        {
            insertionSort();
        }
        else
        {
            printf("Algorithm invalid\n");
            return 1;
        }
        printf("\n\n");
    }
    else if (strcasecmp(argv[1], "selection") == 0)
    {
        selectionSort();
    }
    else if (strcasecmp(argv[1], "bubble") == 0)
    {
        bubbleSort();
    }
    else if (strcasecmp(argv[1], "insertion") == 0)
    {
        insertionSort();
    }
    else
    {
        printf("Usage: %s algorithm", argv[0]);
        return 2;
    }

    printf("Sorted array\n");

    for (int i = 0; i < LENGHT; i++)
    {
        printf("%i\n", array[i]);
    }

    return 0;
}

void swap(int *xp, int *yp)
{
    int temp;

    temp = *xp;
    *xp = *yp;
    *yp = temp;
}

void bubbleSort(void)
{
/* Repeat n-1 times
    For i from 0 to n–2
        If numbers[i] and numbers[i+1] out of order
            Swap them
    If no swaps
        Quit*/

    for (int i = 0; i < LENGHT - 1; i++)
    {
        minIndex = i;
        for (int j = i; j < LENGHT - 2; j++)
        {
            if (array[j] > array[minIndex])
            {
                swap(&array[minIndex], array[j])
            }
        }
    }
}

void selectionSort(void)
{
    for (int i = 0; i < LENGHT - 1; i++)
    {
        int minIndex = i;
        for (int j = i + 1; j < LENGHT; j++)
        {
            if (array[j] < array[minIndex])
            {
                minIndex = j;
            }
        }
        if (minIndex != i)
        {
            swap(&array[minIndex], &array[i]);
        }
    }
}

void insertionSort(void) {}
