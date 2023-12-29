#include <stdio.h>

int main() {

    int low;
    int high;

    do
    {
    scanf("%d %d", &low, &high);
    }
    while(low > high);

    int pages;

    for(pages = low; pages <= high; pages++)
    {
        printf("%d ", pages);
    }

    return 0;
}
