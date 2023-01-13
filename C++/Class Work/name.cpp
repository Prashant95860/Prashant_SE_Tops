#include<iostream>

using namespace std;

class Details{
	public :
		string name;
		
		void getname()
		{
			cout<<"\n Enter Your Name : " ;
			getline(cin,name);
			
		}
		
	void showname()
	{
		cout<<"\n Your Name is : "<<name;
		
	}
};


int main()
{
	Details obj;
	obj.getname();
	obj.showname();

		return 0;
}