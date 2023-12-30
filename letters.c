#include <stdio.h>

int main() {
    char word[50];
    int position;


    fgets(word, 50, stdin);
    scanf("%i", &position);

    printf("%s %c", word, word[position - 1]);

    return 0;
}
