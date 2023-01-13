#include<iostream>
using namespace std;

class person{
	public:
		char name[100];
		int age;
		void per()
		
		{
			cout<<"\nEnter Name : ";
			cin>>name;
			cout<<"\nEnter Age : ";
			cin>>age;
			
		}
	
};


class student : public person{
public:
	int pr=90;
	void percen()
	{
		cout<<"\nThe Percentahe of members who read and write : "<<pr;
		
	}
	
	
};


class teacher :public student{
	public:
		
		void teach()
		{
			cout<<"\n\nSalary : 25000";
			
			
		}
	
	
};


int main()
{
	student obj;
	obj.per();
	obj.percen();
	teacher obj1;
	obj1.teach();
	
	return 0;
}
