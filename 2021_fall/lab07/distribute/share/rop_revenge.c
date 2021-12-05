#include <stdio.h>

void init_prog()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

int main(void)
{
    init_prog();
    puts("reveeeeeeeeeenge!!");
    char buf[0x20] = {0};
    gets(buf);
    
    return 0;
}