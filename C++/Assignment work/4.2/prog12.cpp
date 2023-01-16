#include<iostream>
using namespace std;
int area(int x)
{
	return x*x;
	
}

int area(int l, int b)
{
	return l*b;
}
double area(double r)
{
	return 3.142*r*r;
}
int main()
{
	int x,l,b;
	double r;
	cout<<"Enter the length of square: ";
	cin>>x;
	cout<<"\nEnter the length of rectangle: ";
	cin>>l;
	cout<<"\nEnter width of rectangle: ";
	cin>>b;
	cout<<"\nEnter the radious of circle: ";
	cin>>r;
	cout<<endl<<"The area of square is "<<area(x)<<endl;
cout<<endl<<"\nThe area of rectangle is "<<area(l,b)<<endl;
cout<<endl<<"\nThe area of circle is "<<area(r)<<endl;	
	return 0;
}