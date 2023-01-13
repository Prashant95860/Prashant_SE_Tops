#include<iostream>
using namespace std;

class cricketer{

	 public:
	 
	
	int tt = 200;
	int avg=tt/11;
	 int be = 58;
	
	
	
};

class batsman: public cricketer{
	
	public:
		void display()
{

		cout<<"\nTotal Runs : "<<tt;
		cout<<"\nAverage Runs : "<<avg;
		cout<<"\nBest Performace : "<<be;
		
}
	
};

int main()
{
batsman obj;
obj.display();



	return 0;
}