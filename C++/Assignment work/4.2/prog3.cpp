#include<iostream>
using namespace std;

class line{
	public:
			inline float mul(float a, float b)
			{
				return(a*b);
			}
			inline float cube(float a)
			{
				return(a*a*a);
			}
};

int main()
{
	line obj1;
	float vala,valb;
	cout<<"\nEnter Value : ";
	cin>>vala;
	cout<<"\nEnter Value : ";
	cin>>valb;
	cout<<"\nMultiplication Values are : "<<obj1.mul(vala,valb);
	cout<<"\n\nCube value of ["<<obj1.cube(vala)<<"]["<<obj1.cube(valb)<<"]\n";
		
	return 0;
}