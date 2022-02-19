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
    write(1, "migration revenge!\n", 19);
    read(0, buf, 0x30);
    
    return 0;
}
