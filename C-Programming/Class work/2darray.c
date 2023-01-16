#include<stdio.h>
void main()

{
	int arr1[3][3];
	int i,j;
	printf("\n\n-------Enter 1 Elements-------\n\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("Enter value at index [%d][%d] :",i,j);
			scanf("%d",&arr1[i][j]);
			
		}
	}
	for(i=0;i<3;i++);
	{
		for(j=0;j<3;j++)
		{
			printf("\n Value at index [%d][%d] :%d",i,j,arr1[i][j]);
			
		}
	}
}