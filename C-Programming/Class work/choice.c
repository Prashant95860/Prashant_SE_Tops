#include<stdio.h>

void main()

{
	int a,b,choice;
	printf("\n Enter A & B : ");
	scanf("%d%d" ,&a,&b);
	printf("\nA = %d, B = %d",a,b);
	printf("\n\nPress 1.Addition\nPress 2.Substraction\nPress 3.Multiplication\nPress 4.Division");
	printf("\n\n Enter your choice?");
	scanf("%d",&choice);
	
	switch(choice)
	
	{
		case 1: printf("\nAddition : %d",(a+b));
		break;
		case 2: printf("\nSubstraction : %d",(a-b));
		break;
		case 3: printf("\nMultipliction : %d",(a*b));
		break;
		case 4: printf("\nDivision : %.2f",(float)a/b);
		break;
		default :printf("\nInvalid Choice");
		break;
		
		
	}
	
	
	
}