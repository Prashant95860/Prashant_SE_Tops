#include<stdio.h>
void main()
{
	int n,r,sum=0;
	printf("\nEnter Number : ");
	scanf("%d",&n);
	while(n>0)
	{
		r=n%10;
		sum=sum+r;
		n=n/10;
	}
	printf("Sum of Number is : %d",sum);
	
}