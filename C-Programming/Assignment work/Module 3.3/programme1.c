#include<stdio.h>
void main()
{
	int arr[]={35,13,9,78,60},max=arr[0],i;
	int length = sizeof(arr)/sizeof(arr[0]);

	
	
	
	
		
	for(i=0;i<length;i++)
	
{
	if(arr[i] > max)
	max = arr[i];
	
}
	printf("Maximum Number is : %d",max);
		


}

