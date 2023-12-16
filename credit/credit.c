#include <cs50.h>
#include <stdio.h>

int main(void)
{

    long cardNumber = get_long("Card number: ");
    //AMEX = 34xxxxxxxxxxxxx, 37xxxxxxxxxxxxx
    //Mastercard = 5xxxxxxxxxxxxxxx
    //Visa = 4xxxxxxxxxxxx(xxx)

    int digit[] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16};
    digit[1] = cardNumber % (10^(digit[1]))/(10^(digit[1]-1));

    printf("%i\n", digit[1]);

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
