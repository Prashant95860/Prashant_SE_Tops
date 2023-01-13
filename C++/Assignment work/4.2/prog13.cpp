#include<iostream>
using namespace std;


int main()
{
	int i=5, j=10;
	cout<<"Before swap  A= "<<i<<" B = "<<j<<endl;
	i=i*j;
	j=i/j;
	i=i/j;
	cout<<"After swap A= "<<i<<" B = "<<j<<endl;
	return 0;
}