#include <stdio.h>

int main() {
    //your code goes here
    float bmi;

    printf("Enter BMI: ");
    scanf("%f", &bmi);

    if(bmi < 18.5)
    {
        printf("Underweight \n");
    }
    else if(bmi > 25)
    {
        printf("Overweight \n");
    }
    else
    {
        printf("Normal");
    }

    return 0;
}
