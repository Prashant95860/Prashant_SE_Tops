#include<stdio.h>
void main()
{
	int a[10],i;
	int evencount=0,Oddcount=0;

		
			printf("\n Enter the any 10 Elements\n");
			
			
	
			for(i=0;i<10;i++)
			{
				scanf("%d",&a[i]);
			
		
				if(a[i]%2==0)
				 evencount++;
			
				else
			
					Oddcount++;
					
				
			}
		
printf("\n Total Even number is : %d",evencount);
printf("\n Total Odd number is : %d",Oddcount);
}