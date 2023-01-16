#include<iostream>

using namespace std;

class Box{
	public:
		double width,height,depth;
		Box()
		{
			cout<<"Default Constructor Called.";
			width=5;
			height=4;
			depth=6;
			
		}

void display()
{
	cout<<"\nVolume is "<<(width*height*depth);
	
}
};









int main()
{
	Box obj;
	obj.Box();
	return 0;
}

