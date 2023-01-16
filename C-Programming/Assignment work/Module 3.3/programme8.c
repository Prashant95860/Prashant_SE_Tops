#include<stdio.h>
void main()
{
	char n,c,s=0,r;
	printf("\nEnter Number : ");
	scanf("%d",&n);
	
c=n;
while(n>0)
{
	r=n%10;
	s=r+(s*10);
	n=n/10;
}
if(c==s)
printf("Palindrome Number");
else
printf("Not");








}