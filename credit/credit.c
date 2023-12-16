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
    int divisor = 10;

    for (i = 0; i < 16; i++)
    {
        digit[i] = cardNumber % (divisor*10 e i + 1);

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
