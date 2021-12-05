#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
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
    
    printf("Give me your name: ");
    read(STDIN_FILENO, name, 0x40);

    printf("Hi %s, can you hack me?\n", name);
    read(STDIN_FILENO, buf, 0x40);
    printf("Ha, this can't hack me!\n");
    printf("%s\n", buf);
    printf("Give your one more chance. Hack me!\n");
    read(STDIN_FILENO, buf, 0x40);
    
    return 0;
}