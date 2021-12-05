#include <stdio.h>
#include <unistd.h>

void init_prog()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

int main(void)
{
    init_prog();
    char buf[0x20] = {0};

    // puts("reveeeeeeeeeenge!!");
    write(1, "migration!\n", 12);
    read(0, buf, 0x50);
    
    return 0;
}