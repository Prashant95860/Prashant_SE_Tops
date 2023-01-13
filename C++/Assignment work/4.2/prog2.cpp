#include<iostream>
#include<string.h>
using namespace std;
class bank{
	int acno;
	char name[100],acctype[100];
	float bal;
	public:
		bank(int accnum, char*nm,char*acc_type,float balance)
		{
			acno=accnum;
			strcpy(name,nm);
			strcpy(acctype,acc_type);
			bal=balance;
			
		}
	void deposit();
	void withdraw();
	void display();
};	
	

void bank::deposit()
{
	int da1;
	cout<<"\n Enter Deposit Amount : ";
	cin>>da1;
	bal+=da1;
	
}

void bank::withdraw()
{
	int wd1;
	cout<<"\n Enter Withdraw Amount : ";
	cin>>wd1;
	if(wd1>bal)
	cout<<"\n Invalid Tranjaction";
    bal-=wd1;
	
}

void bank::display()
{
	cout<<"\n--------------";
	cout<<"\n Account No :"<<acno;
	cout<<"\n Name :"<<name;
	cout<<"\n Acount Type :"<<acctype;
	cout<<"\n Balance :"<<bal;
}



int main()
{
	int accnum;
	char name[100],acc_type[10];
	float balance;
	cout<<"\n Name of the depositer : ";
	cin>>name;
	cout<<"\n Account No :";
	cin>>accnum;
	cout<<"\n Account Type :";
	cin>>acc_type;
	cout<<"\n Balance Amount in the account :";
	cin>>balance;
 
	bank obj(accnum,name,acc_type,balance);
	obj.deposit();
	obj.withdraw();
	obj.display();
	
return 0;
}





















