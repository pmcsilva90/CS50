#include <stdio.h>

int main() {
    // number of tickets ordered
    int tickets; // take it from input

    scanf("Number of tickets: %d", &tickets);

    // price per ticket
    float price = 7.45;

    float total = tickets * price;

    printf("Total: %f", total);

    return 0;
}
