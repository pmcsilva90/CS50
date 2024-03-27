#include <stdio.h>


int main() {
    int mileage;
    int months;

    printf("Input mileage: ");
    scanf("%d", &mileage);

    printf("Months since last oil change: ");
    scanf("%d", &months);

    if(mileage > 10000 || months > 12)
    {
        printf("Change oil");
    }
    else
    {
        printf("OK");
    }
    return 0;
}
