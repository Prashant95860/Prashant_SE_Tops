#include<iostream>
#include<string.h>
using namespace std;

class String{
	private:
		char str[50];
		public:
		String()
			{
				strcpy(str," ");
			}
			
	
	String(char s[]){
		
		
		strcpy(str,s);
		
	}
void getstr()
{
	cout<<"Enter String : ";
	cin.getline(str,50);
	}	
	
	
	String operator+(String objs)
	{
		String temp;
		if(strlen(temp.str) + strlen(objs.str)<50)
		{
			strcpy(temp.str,str);
			strcat(temp.str,objs.str);
		}
		else{
			cout<<"String over flow";
			exit(1);
		}
		return temp;
		
	}
	void display()
	{

	cout<<str<<endl;
}
};



int main()
{

	
	String s1;
	String s2;
	cout<<"Enter obj1 string"<<endl;
	s1.getstr();
		s1.display();
		cout<<"\nEnter Obj2 string"<<endl;
		s2.getstr();
	s2.display();
	String s3;
	s3 =s1+s2;
	s3.display();
	
return 0;	
}