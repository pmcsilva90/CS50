#include <stdio.h>

int main() {
    char word[50];
    int position;


    fgets(word, 50, stdin);
    scanf("%i", &position);

    printf("%s %i", word, word[position]);

    return 0;
}
