#include<iostream>
using namespace std;
class staticdemo{
	public:
		static int objcount;
		
		staticdemo()
		{
			cout<<"This is Default Constructor";
			objcount++;
			
			
		}
};





int staticdemo::objcount=0;



int main()
{
	staticdemo obj1,obj2,obj3;
	cout<<"\nObject Count : "<<obj1.objcount;
	return 0;
	
}