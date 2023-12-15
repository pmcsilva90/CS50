#include <cs50.h>
#include <stdio.h>

int main(void)
{

    long cardNumber = get_long("Card number: ");
    //AMEX = 34xxxxxxxxxxxxx, 37xxxxxxxxxxxxx
    //Mastercard = 5xxxxxxxxxxxxxxx
    //Visa = 4xxxxxxxxxxxxxxx

    if (cardNumber >= 340000000000000 && cardNumber < 350000000000000)
    {
        printf("AMEX\n");
    }
    else
    {
        printf("INVALID\n");
    }
}
