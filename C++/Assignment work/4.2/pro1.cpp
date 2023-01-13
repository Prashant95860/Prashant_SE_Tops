#include<iostream>
using namespace std;
int main()
{
	char op;
	double a,b;
	
	cout<<"\nEnter A : ";
	cin>>a;
	cout<<"\n\nEnter B : ";
	cin>>b;
	cout<<"\nEnter your choice? \n1.Addition,\n2.Substraction,\n3.Multipliaction,\n4.Division :\n\n";
	cin>>op;

	
	switch(op)
	{
		case '1':
		cout<<a<<"+"<<b<<"="<<(a+b);
		break;
		case '2':
		cout<<a<<"-"<<b<<"="<<(a-b);
		break;
		case '3':
		cout<<a<<"x"<<b<<"="<<(a*b);
		break;
		case '4':
		cout<<a<<"/"<<b<<"="<<(a/b);
		break;
		
			
		
	}
	
	
	
	return 0;
	
}