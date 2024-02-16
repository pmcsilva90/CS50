#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long card = get_long("Number: ")

    // AMEX: 15 digit, 34 or 37
    // Mastercard: 16 digit, 51, 52, 53, 54, 55
    // Visa: 13 and 16 digit, 4

    if(card / 10000000000000 == 34 || card / 10000000000000 == 37)
    {
        printf()
    }
}
