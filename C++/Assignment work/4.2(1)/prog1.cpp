#include<iostream>
using namespace std;
template<class t>
void swap1(t &i,t &j)
{
	t temp;
	temp=i;
	i=j;
	j=temp;
}

int main()
{
		int i=5, j=10;
	cout<<"Before swap  A= "<<i<<" B = "<<j<<endl;
	cout<<"\nAfter swap A= "<<i<<" B = "<<j<<endl;
	return 0;

}