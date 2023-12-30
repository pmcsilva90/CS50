#include <stdio.h>

int main() {
    char word[50];
    int position = 0;


    fgets(word, 50, stdin);

    printf("%s %d", word, word[position]);

    return 0;
}
