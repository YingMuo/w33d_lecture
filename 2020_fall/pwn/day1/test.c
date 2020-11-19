#include <stdio.h>
#include <stdlib.h>

int add( int a, int b )
{
	return a+b;
}

int main()
{
	setvbuf( stdin, NULL, _IONBF, 0 );
	setvbuf( stdout, NULL, _IONBF, 0 );
	setvbuf( stderr, NULL, _IONBF, 0 );
	int a = 0;
	int b = 0;
	char str[30] = {0};
	printf( "input: " );
	// scanf( "%d %d", &a, &b );
	// printf( "%d\n", add( a, b ) );
	scanf( "%s", str );
	printf( "%s\n", str );
	printf( "%lu\n", *(unsigned long*)(str) );
	printf( "%lx\n", *(unsigned long*)(str) );
		
	return 0;
}
