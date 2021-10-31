#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/mman.h>

void init_prog()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

int main(void)
{
    init_prog();
    char buf[0x10] = {0};
    char *name = mmap((void *)0x410000, 0x1000, PROT_EXEC | PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (name == (void *)-1)
    {
        perror("mmap failed");
    }
    
    puts("Give me your name: ");
    fgets(name, 0x40, stdin);
    if (name[strlen(name)-1] == '\n')
        name[strlen(name)-1] = '\0';

    printf("Hi %s, can you hack me?\n", name);
    fgets(buf, 0x40, stdin);
    if (buf[strlen(buf)-1] == '\n')
        buf[strlen(buf)-1] = '\0';
    
    return 0;
}
