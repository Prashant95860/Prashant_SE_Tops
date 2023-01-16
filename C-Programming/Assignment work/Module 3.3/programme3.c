#include<stdio.h>
void main()
{
	char st[20],temp;
	int a,b;
	
	printf("\nEnter the string : ");
	scanf("%s",&st);
	
	a=0;
	b=strlen(st)-1;
	while (a<b)
	{
		temp = st[a];
		st[a]=st[b];
		st[b]=temp;
		a++;
		b--;
		
	}
	printf("\n Reverse string is : %s",st);
	
}