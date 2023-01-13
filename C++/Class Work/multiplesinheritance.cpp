#include<iostream>
using namespace std;
class Student{
	public:
		string name;
		
		void getName()
		{
			cout<<"Enter Name : ";
			cin>>name;
		}
};
class ExtraMarks{
	public:
		int sp;
		ExtraMarks()
		{
			sp=60;
			
		}
};
class Result : public Student,public ExtraMarks
{
	public:
		int s1,s2,s3,total;
		float percentage;
		Result()
		{
			s1=76;
			s2=74;
			s3=73;
			total=s1+s2+s3+sp;
			percentage=(float)total/4;
			
		}	
	

void dispaly()
{
	cout<<"\nName : "<<name;
	cout<<"\nTotal : "<<total;
	cout<<"\nPercentage : "<<percentage;
	 
}

};

int main()
{
	Result obj;
	obj.getName();
	obj.dispaly();
	
	return 0;
}