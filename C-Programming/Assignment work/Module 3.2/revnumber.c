#include<stdio.h>
void main()
{
	int n,reverse=0,remainder,revnumber;
	printf("Enter Digit : ");
	scanf("%d",&n);
	while (n !=0)
	{
		remainder =n%10;
		revnumber = revnumber*10+remainder;
		n=n/10;
		
	}
	
	printf("\n The Reverse Number is : %d",revnumber);
	
}