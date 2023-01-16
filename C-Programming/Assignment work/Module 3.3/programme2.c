#include<stdio.h>
void main()
{
	int a,b,pr;
	char choice;
	
	printf("\nEnter A : ");
	scanf("%d",&a);
	printf("\nEnter B : ");
	scanf("%d",&b);
	printf("\n A = %d, B = %d",a,b);
	printf("\n\nPress 1. Addition\nPress 2. Substraction\nPress 3. Multiplication\nPress 4. Division");
	printf("\n\nPress as per your choice?: ");
	scanf("%d",&pr);
	
	switch(pr)
	{
		case 1:printf("\nAddition : %d",(a+b));
		break;
		case 2:printf("\nSubstraction : %d",(a-b));
		break;
       case 3:printf("\nMultiplication : %d",(a*b));
		break;
       case 4:printf("\nDivision : %d",((float)a/b));
		break;

default :printf("\nInvalid Choice ");
break;


	}
	
}