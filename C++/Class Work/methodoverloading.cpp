#include<iostream>
using namespace std;
class MO{
	public:
		void demo()
		{
			int a = 10;
			cout<<"A = "<<a;
			
		}
		
		void demo(int a)
		{
			if (a%2==0)
			{
				cout<<"\nIt is Even";
				
			}
			else
			{
				cout<<"\nIt is Odd";
			}
		}
		
		
		int demo(int a,int b)
		{
			return a+b;
		}
		
};


int main()
{
	MO obj;
	obj.demo();
	obj.demo(51);
	cout<<"\nAddition : "<<obj.demo(54,69);
	
	return 0;
	
}