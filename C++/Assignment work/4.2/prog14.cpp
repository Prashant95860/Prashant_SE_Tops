#include<iostream>
using namespace std;
class max{
	private:
	 int a,b;
		friend int number(data)
		public:
		{
			cout<<"Enter A : ";
			cin>>a;
			cout<<"Enter B : ";
			cin>>b;
		}
	
		
};

int data(max o)
{
	if(o.a>o.b)
	{
		cout<<"Largest number is : "<<o.a;
	}
	else
	{
		cout<<"Largest number is : "<<o.b;
	}
}




int main()
{
	max o;
	o.number();
	data(o);
	return 0;
}