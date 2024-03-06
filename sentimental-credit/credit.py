from cs50 import get_int

card = get_int("Number: ");

# AMEX: 15 digit, starting 34 or 37
# Mastercard: 16 digit, starting 51, 52, 53, 54 or 55
# Visa: 13 and 16 digit, starting 4

digits = card
checksum = 0

while digits > 0:
    checksum += digits % 10
    digits /= 10
    if digits % 10 * 2 > 9:
        checksum += digits % 10 * 2 % 10 + digits % 10 * 2 / 10
    else:
        checksum += digits % 10 * 2
    digits /= 10

if (checksum % 10 == 0)
{
    if (card / 10000000000000 == 34 || card / 10000000000000 == 37)
    {
        printf("AMEX\n");
    }
    else if (card / 100000000000000 >= 51 && card / 100000000000000 <= 55)
    {
        printf("MASTERCARD\n");
    }
    else if (card / 1000000000000 == 4 || card / 1000000000000000 == 4)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}
else
    printf("INVALID\n");

