#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void init_prog()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

int main(void)
{
    init_prog();

    char name[0x20] = {0};

    puts("no buffer here : )\n");

    printf("Give me your name: ");
    fgets(name, 0x20, stdin);
    if (name[strlen(name)-1] == '\n');
        name[strlen(name)-1] = '\0';
    
    unsigned long addr = 0;
    unsigned long value = 0;
    printf("peep the address: ");
    scanf("%lx", &addr);
    printf("your value: %lx\n", *(unsigned long *)addr);

    printf("set the address: ");
    scanf("%lx", &addr);
    printf("value is: ");
    scanf("%lx", &value);
    *(unsigned long *)addr = value;

    puts("bye,");
    puts(name);

    return 0;
}