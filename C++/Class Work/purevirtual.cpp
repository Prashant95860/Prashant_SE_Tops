#include<iostream>
using namespace std;
class Demo{
	public:
	void f1()
	{
		cout<<"\nNone pure virtual function";
		
	}
	virtual void f2();
	
};
class Sample : public Demo{
public:
	void f3()
	
{
	cout<<"\nNone pure virtual function in sample class";
	
	}	
	void f2()
	{
		cout<<"\nPure virtual function implimented";
		
	}
};





int main()
{
	Sample obj;
	obj.f1();
	obj.f2();
	obj.f3();
	return 0;
}