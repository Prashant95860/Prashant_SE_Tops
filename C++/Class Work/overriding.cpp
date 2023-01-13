#include<iostream>
using namespace std;
class A{
	public:
		void show()
		{
			cout<<"\nThis is A";
		}
};
class B :public A{
	public:
	void show()
		{
A::show();
			cout<<"\nThis is B ";
			 
		}
};

class C : public B{
	public:
	void show()
		{
		B::show();
			cout<<"\nThis is C";
			
		}
		
};








int main()
{
	C obj;
	obj.show();
	return 0;
}