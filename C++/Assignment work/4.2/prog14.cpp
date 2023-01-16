#include<iostream>
using namespace std;

class Large{
	private:
		int i,j;
		public:
		void input(){
			cout<<"Enter A: ";
			cin>>i;
			cout<<"Enter B: ";
			cin>>j;
		}
		friend void data(Large t);
};
void data(Large t){
	if(t.i>t.j)
	{
		
		cout<<"\nLargest number is: " <<t.i;
	}
	else {
		cout<<"\nLargest number is: " <<t.j;
	}
	
}
int main()
{
	Large t;
	t.input();
	data(t);
	return 0;
}