#include <stdio.h>

int main() {
    char dir;
    scanf("%c", &dir);

    switch(dir)
    {
        case 'w':
        printf("Up");
        break;
        case 'a':
        printf("Left");
        break;
        case 'd':
        printf("Right");
        break;
        case 's':
        printf("Down");
        break;
        default:
        printf("Wrong");
        break;
    }

    return 0;
}