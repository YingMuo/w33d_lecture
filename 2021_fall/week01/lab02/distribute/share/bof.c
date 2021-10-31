#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void init_prog()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void debug()
{
    system("sh");
}

int main(void)
{
    init_prog();
    char buf[0x20] = {0};
    printf("Can you hack me?\n");
    gets(buf);

    return 0;
}