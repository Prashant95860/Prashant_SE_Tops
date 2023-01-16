#include<iostream>
using namespace std;

class cricketer{
public:
	int tot,avg,be;
void data()

	{
	tot=200;
	avg=200/11;
	be=52;
	
}


	
};

class batsman : public cricketer{

public:
	void score()
	{
	
	cout<<"Total Runs of Team :  ";
	cin>>tot;
	cout<<"Average Run : ";
	cin>>avg;
	cout<<"Best Perfomace : ";
	cin>>be;
}
	void display()
	{
		cout<<"\nTotal Runs :  "<<tot;
		cout<<"\nAverage Run : "<<avg;
		cout<<"\nBest Performance : "<<be;
	}
	
};



int main()
{
	batsman obj;
	obj.display();	
	return 0;
}