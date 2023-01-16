#include<stdio.h>
void main()
{
	int a,b,k=6;
	
	for(a=0;a<k;a++)
	{
		for(b=0;b<a+1;b++)
		
			printf(" *");
			printf("\n");
		
	}
	for (a=1;a<k;a++)
	{
		for(b=a;b<k;b++)
		
			printf(" *");
			printf("\n");
		
	}
}