#include<stdio.h>
void main()
{
	int a,b;
	printf("Enter A : ",a);
	scanf("%d",&a);
	printf("Enter B : ",b);
	scanf("%d",&b);
	printf("\nBefore swaping value First Number is %d and Second Number is %d ",a,b);
	a=a+b;
	b=a-b;
	a=a-b;
	
	printf("\n\nAfter Swap Value is : A=%d,B=%d",a,b);
	
	
	
}