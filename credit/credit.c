#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{

    long cardNumber = get_long("Card number: ");
    //AMEX = 34xxxxxxxxxxxxx, 37xxxxxxxxxxxxx
    //Mastercard = 5xxxxxxxxxxxxxxx
    //Visa = 4xxxxxxxxxxxx(xxx)

    int digit[16];
    long divisor;
    long subtractor;
    int i;

    for (i = 0 ; i < 16; i++)
    {
        divisor = pow(10, i + 1);
        subtractor = pow(10, i);
        digit[i] = cardNumber % divisor / subtractor;

        printf("%d\n", digit[i]);
    }

    printf("\n");

    for (i=1 ; i < 16; i = i + 2)
    {
        digit[i] = digit[i] * 2;

        printf("%d\n", digit[i]);
    }

    





    if (cardNumber >= 340000000000000 && cardNumber < 350000000000000)
    {
        printf("AMEX\n");
    }
    else if (cardNumber >= 370000000000000 && cardNumber < 380000000000000)
    {
        printf("AMEX\n");
    }

    else if (cardNumber >= 5100000000000000 && cardNumber < 5600000000000000)
    {
        printf("Mastercard\n");
    }

    else if (cardNumber >= 4000000000000000 && cardNumber < 5000000000000000)
    {
        printf("Visa\n");
    }

    else if (cardNumber >= 4000000000000 && cardNumber < 5000000000000)
    {
        printf("Visa\n");
    }

    else
    {
        printf("INVALID\n");
    }
}
