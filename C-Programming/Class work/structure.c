#include<stdio.h>

struct Employee{
	int eid;
	char name[10];
	float sal;
	
};


void main()
{
struct Employee a;
printf("\nEnter ID : ");
scanf("%d",&a.eid);
printf("\nEnter Name : ");
scanf("%s",&a.name);
printf("\nEnter Salary : ");
scanf("%f",&a.sal);

printf("\n\nID : %d",a.eid);
printf("\nName : %s",a.name);
printf("\nSalary : %.2f",a.sal);
	
}