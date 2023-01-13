#include<iostream>
using namespace std;

class Avadh{
private:
	int money;
	friend int Siddhant(Avadh);
	public:
		Avadh()
		{
			money=0;
	}
};

int Siddhant(Avadh a)
		{
			a.money=5000;
			return a.money;
			
		}


int main()
{
Avadh obj;
cout<<"Money given is "<<Siddhant(obj);

	return 0;
	
}