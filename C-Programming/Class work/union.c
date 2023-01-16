#include<stdio.h>

union Employee{
	int eid;
	char name[10];
	float sal;
	
};


void main()
{
union Employee a;
printf("\nEnter ID : ");
scanf("%d",&a.eid);
printf("ID : %d",a.eid);
printf("\nEnter Name : ");
scanf("%s",&a.name);
printf("Name : %s",a.name);
printf("\nEnter Salary : ");
scanf("%f",&a.sal);
printf("Salary : %.2f",a.sal);
	
}