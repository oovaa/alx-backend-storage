#include <stdio.h>

int main(int argc, char *argv[])
{
	int a, c, b;
	printf("enter num 1: \n");
	scanf("%d", &a);
	printf("enter num 2: \n");
	scanf("%d", &b);
	printf("enter num 3: \n");
	scanf("%d", &c);

	if (a > b && a > c)
	{
		printf("max is a: %d\n", a);
	}
	else if (b > a && b > c)
	{
		printf("max is b: %d\n", b);
	}
	else
	{
		printf("max is c: %d\n", c);
	}

	return 0;
}