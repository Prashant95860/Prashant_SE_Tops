#include<iostream>
using namespace std;


template <typename T>
T add(T a,T b)
{
	return a+b;
}


int main()

{
	cout<<add<int>(10,50);
	cout<<"\n"<<add<float>(10.5f,50.8f);
	cout<<"\n"<<add<string>("tops","tech");
	
	
	
	return 0;
}