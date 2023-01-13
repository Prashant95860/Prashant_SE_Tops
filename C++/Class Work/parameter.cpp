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

Box(double w,double h,double d)
{
	cout<<"\n\nParameterized Constructor Called";
	width=w;
	height=h;
	depth=d;
	
}

Box(const Box &h)
{

	cout<<"\n\nCopy Constructor is Called.";
	width=h.width;
	height=h.height;
	depth=h.depth;

}
void display()
{
	cout<<"\nVolume is "<<(width*height*depth);
	
	}	
	
	
	
};


int main()
{

Box obj1,obj2;
obj1.display();
Box obj3(5,2,6);

obj3.display();
Box obj4(obj1);
obj4.display();


	return 0;
	
}