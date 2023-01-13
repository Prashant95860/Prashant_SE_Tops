#include<iostream>
using namespace std;

class students{
	public:
	int rollno;
	void info()
		{
			cout<<"Roll Number : ";
			cin>>rollno;
					
		}
	
};

class TestScores{
public:
int s1;
int s2;
void marks()
{
	s1=78;
	s2=83;
	
	}	
};
	
class Result : public students,public TestScores{
	public:
		int s1,s2,Total;
		 Result()
		{
		s1=78;
	    s2=83;
		Total=s1+s2;
			
		}
		
		void data()
		{
			cout<<"\n Roll Number : "<<rollno;
			cout<<"\nMath : "<<s1;
			cout<<"\nEnglish : "<<s2;
			cout<<"\n Total : "<<Total;
		}
};



int main()
{

Result obj;
obj.info();
obj.data();


	return 0;
}