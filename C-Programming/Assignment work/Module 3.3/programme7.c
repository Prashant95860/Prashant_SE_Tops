#include<stdio.h>
void main()
{
	char st[40],i;
	printf("\nEnter string : ");
	scanf("%s",&st);
	
	for(i=0;st[i]!='\0';i++)
	printf("\nLength of string : %d",i);
	
}