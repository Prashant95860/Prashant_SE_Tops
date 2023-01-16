#include<stdio.h>
void main()
{
	int weekday;
	printf("Enter the Day Number 1 to 7 (consider 1= Monday, and 7= Sunday) :  ");
	scanf("%d",&weekday);
	
	


	
	switch(weekday)
{
case 1:	printf("Monday");
	break;
case 2:	printf("Tuesday");
	break;
case 3:	printf("Wednesday");
	break;
case 4:	printf("Thuresday");
	break;
case 5:	printf("Friday");
	break;
case 6:	printf("Saturday");
	break;
case 7:	printf("Sunday");
	break;
	default:("\n Please Enter Valid Number between 1 to 7");
	
	
}
}


