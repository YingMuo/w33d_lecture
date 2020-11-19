#include <stdio.h>
#include <stdlib.h>

void callme()
{
	system( "/bin/sh" );
	return;
}

int main()
{
	char buf[0x20] = {0};
	gets( buf );
	return 0;
}
