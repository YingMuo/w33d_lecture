#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <signal.h>
#include <time.h>

void handler(int sig)
{
    printf("boom!!\n");
    exit(0);
}

void init_prog()
{
    signal(SIGALRM, handler);
    alarm(10);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void print_flag()
{
    char flag[0x20] = {0};
    int fd = open("/home/guess/flag", O_RDONLY);
    read(fd, flag, 0x20);
    printf("this is your flag: %s\n", flag);
}

int main(void)
{
    init_prog();

    int number = rand;
    number %= 1000000;
    if (number < 0)
        number *= -1;

    int guess = -1;
    while (1)
    {
        printf("guess a number: ");
        scanf("%d", &guess);

        if (guess == number)
        {
            printf("correct!!\n");
            print_flag();
            break;
        }
        else if (guess > number)
        {
            printf("too big!!\n");
        }
        else
        {
            printf("too small!!\n");
        }
    }
    

    return 0;
}
