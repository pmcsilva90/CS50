#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input);

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("%i\n", convert(input));
}

// Convert positive integer as a string to an integer using recursion
int convert(string input)
{

    int n = strlen(input) - 1;
    int result = 0;

    // Base case: when the string is empty
    if (n < 0)
    {
        return 0;
    }

    // Convert the last character to an integer
    result = input[n] - '0';
    if (n > 0)
    {
        n = n - 1;
    }

    // Recursively convert the substring without the last character
    return result + 10 * convert(input);
}
