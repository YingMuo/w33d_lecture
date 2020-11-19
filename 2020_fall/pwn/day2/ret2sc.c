#include <stdio.h>
#include <string.h>

char content[40] = {};

int main() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    char name[16] = {};
    printf("Enter your name > ");
    fgets(name, 40, stdin);
    printf("What do you want to say? > ");
    fgets(content, 40, stdin);

    if(name[strlen(name)-1] == '\n')
        name[strlen(name)-1] = 0;
    if(content[strlen(content)-1] == '\n')
        content[strlen(content)-1] = 0;

    printf("%s say : %s\n", name, content);
    return 0;
}
