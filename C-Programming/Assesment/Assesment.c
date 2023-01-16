#include<stdio.h>    
  
void main()
{  
int a[10][10],b[10][10],mul[10][10],r,c,i,j,k;    

printf("\n\n----------Matrix 1 Elemnts : ----------\n\n");

printf("Enter Elements\n"); 
   
for(i=0;i<2;i++)    
{    
for(j=0;j<2;j++)    
{    
scanf("%d",&a[i][j]);    
}    
}  
  
printf("\n\n----------Matrix 2 Elemnts : ----------\n\n");

printf("Enter Elements\n");  
  
for(i=0;i<2;i++)    
{    
for(j=0;j<2;j++)    
{    
scanf("%d",&b[i][j]);    
}    
}    
    
printf("\n\n----------Result: Multiplication  Matrix : ----------\n\n");  
 
for(i=0;i<2;i++)    
{    
for(j=0;j<2;j++)    
{    
mul[i][j]=0;    
for(k=0;k<2;k++)  
  
{    
mul[i][j]+=a[i][k]*b[k][j];    
}    
}    
}    
   
for(i=0;i<2;i++)    
{    
for(j=0;j<2;j++)    
{    
printf("%d\t",mul[i][j]);    
}    
printf("\n");    
}    
 
}  
