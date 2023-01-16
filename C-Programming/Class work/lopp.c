#include<stdio.h>
void main()
{
	int i,j;
	
		for(i=2;i<=7;i++)
		{
			printf("\n\nTable of %d\n",i);
			
			
			for(j=1;j<=10;j++)
			{
				printf("\n%d x %d = %d",i,j,i*j);
				
			}
		}

}