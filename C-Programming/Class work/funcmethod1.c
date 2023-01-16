#include<stdio.h>

void func1()
{
	printf("\n This is Func1");
}
void func2()
{
	printf("\n This is Func2");
}
void func3()
{
	printf("\n This is func3");
	func2();
	
}

void main()
{
	func1();
	func2();
	func3();
	
}