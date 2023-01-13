#include<iostream>
using namespace std;

class Scopedemo{
	public:
		void func();
		void func2()
		{
		cout<<"This is func2";
		}
};
void Scopedemo::func()
{
	cout<<"\nThis is Function from demospace";
	Scopedemo::func2();
	
}



int main()
{
	Scopedemo obj;
	obj.func();
	return 0;
}