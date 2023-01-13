#include<iostream>
using namespace std;
class Calc{
	public:
	int a,b;
	Calc()
	
	{
		cout<<"\nEnetr A : ";
		cin>>a;
		cout<<"\nEnter B : ";
		cin>>b;
		
		cout<<"\nAddition : "<<a+b;
		cout<<"\nSubstraction : "<<a-b;
		cout<<"\nMultiplication : "<<a*b;
		cout<<"\nDivision : "<<float(a/b);
		
		
	}
	};




int main()
{
	
Calc obj;
	return 0;
}