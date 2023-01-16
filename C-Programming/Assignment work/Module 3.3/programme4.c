#include<stdio.h>
int multiply(int n);
void main() {
    int n;
    printf("Enter Number: ");
    scanf("%d",&n);
    printf("\nFactorial of number is %d = %d", n, multiply(n));
    
}

int multiply(int n) {
    if (n>=1)
        return n*multiply(n-1);
    else
        return 1;
}
