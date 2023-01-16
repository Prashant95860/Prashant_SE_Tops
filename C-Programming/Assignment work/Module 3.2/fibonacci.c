#include<stdio.h>
void main()
{
	int i,n,next,valuea=0,valueb=1;
	printf("\nEnter the number  : ");
	scanf("%d",&n);
	
	printf("\nFibonacci Series is :\n\n\n %d %d",i,valuea,valueb);
	i=2;
	while(i<n)
	
	{
		next=valuea+valueb;
		valuea=valueb;
		valueb=next;
		i++;
		printf("%d\t",next);
		
	}
	
}