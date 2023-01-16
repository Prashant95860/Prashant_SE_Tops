#include<stdio.h>
#include<string.h>
void main()
{
	char fname[10]="tops";
	char lname[10]="CG ROAD";
	char str3[10];
	char str1[10]="animal";
	char str2[10]="ZOO";
	
printf("\nString 1 : %s",fname);
printf("\nString 2 : %s",lname);
printf("\n\nString1 Length : %d",strlen(fname));
printf("\nString Reverse : %s",strrev(fname));
printf("\nString copy : %s",strcpy(str3,lname));
printf("\nString Concatenate : %s",strcmp(str1,str2));
printf("\nString Upper Case : %s",strupr(str1));
printf("\nString Lower case : %s",strlwr(str2));

}