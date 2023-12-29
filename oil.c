#include <stdio.h>
/*You are making an app that should remind you when its the time to change the oil in your car.

The oil needs to change if the mileage after the last change is over 10.000, or if the last oil change has been over 12 months ago.

Task:

Take the mileage and months values from input and output "Change Oil", in case the conditions above are satisfied.

In case its not the time for an oil change, output "OK".*/

int main() {
    int mileage;
    int months;

    printf("Input mileage: ");
    scanf("%d", &mileage);

    printf("Months since last oil change: ");
    scanf("%d", &months);

    if(mileage > 10000 || months > 12)
    {
        printf("Change oil")
    }

    return 0;
}
