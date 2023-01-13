#include<iostream>
#include<time.h>

using namespace std;
class Firstscreen{
public :
int ch;
int pin=12345;
int ep;
int i;
int acess;
Firstscreen()
{
	time_t t;
	time(&t);
	cout<<"---------WELCOME TO ATM------------";
	cout<<"\n  --------------------";
	cout<<"\n\nCurrent date : "<<ctime(&t);
	cout<<"\n   -----------------";
	 cout<<"-------------------------------";
	 cout<<"\nPress 1 and then Press Enter to Access Your Number";
	 cout<<"\n           or";
	 cout<<"\nPress 0 and press Enter to get help";
	 cout<<"\n\n Press Button : ";
	 cin>>ch;
	 switch (ch)
	 {
	 
	 case(1):
     cout<<"\n\n---------ATM ACCOUNT ACCESS------------";	 
	 cout<<"\nEnter Your Account Pin Number! [Only one attempt is allowed]";
	 cout<<"\n--------------------------------------\n";
	 cin>>ep;
	 break;
	 case (0):
	 cout<<"\n\n---------ATM ACCOUNT STATUS------------";
	 cout<<"\nYou must have the correct pin number to access this account.";
	 cout<<"\nSee your bank representative for assistance during bank opening hours";
	 cout<<"\nThanks for, your choice today";
	  break;
	  
	 } 
     
     if (ep==pin)
{
	for(i=0;i>=0;i++)
{
	
	cout<<"\n\n---------ATM MENU SCREEN------------";
	 cout<<"\nEnter [1] to Deposit cash";
	cout<<"\nEnter [2] to Withdraw cash";
	cout<<"\nEnter [3] for Balance Inquiry";
	cout<<"\nEnter [0] to Exit ATM";
	cout<<"\n\nPLEASE ENTER A SELECTION AND PRESS RETURN KEY : ";     	
    cin>>acess;
    int balance = 20000;
    
	int de;
	int wh;
	int debited;
    switch(acess)
      {
      	case(1):
						cout<<"\n\n---------ATM ACCOUNT DEPOSIT SYSTEM------------";
						cout<<"\nThe names of the Account Holder is : Rakesh Kharva";
						cout<<"\nThe Account Holder's address is : Mumbai";
						cout<<"\nThe Branch Location is : Andheri";
						cout<<"\nAccount number is : 5678";
						cout<<"\n\n---------------------------------------------";
						cout<<"\n\nPresent available balance  : RS "<<balance;
						cout<<"\n\nEnter the amount to be deposited : ";
						cin>>de;
						int tot;
						tot = balance + de;
						cout<<"\nYour new available balance amount is RS "<<tot;
						cout<<"\n\n             THANK YOU                  ";
						cout<<"\n\nPRESS ANY KEY TO RETURN TO THE MAIN MENU";
						break;
					case(2):
						cout<<"\n\n---------ATM WITHDRAWAL SYSTEM------------";
						cout<<"\nThe names of the Account Holder is : Rakesh Kharva";
						cout<<"\nThe Account Holder's address is : Mumbai";
						cout<<"\nThe Branch Location is : Andheri";
						cout<<"\nAccount number is : 5678";
						cout<<"\n------------------------------------------------";
						cout<<"\n\nPresent available balance  : RS "<<balance;
						cout<<"\nEnter Amount of Withdrawal : ";
						cin>>wh;
						if (wh > balance)
						{
							cout<<"Insufficient Balance in Your Account \n Sorry!!!";
						}
						else
						{
							cout<<"\n\nWithdrawal is Successfull";
							debited=balance-wh;
							cout<<"\n\nAvailable balance is : RS "<<debited;
						}
						cout<<"\n\nPRESS ANY KEY TO RETURN TO THE MAIN MENU";
						break;
					case(3):
						cout<<"\n------------- ATM BALANCE INQUIRY SYSTEM ----------------";
						cout<<"\nThe names of the Account Holder is : Rakesh Kharva";
						cout<<"\nThe Account Holder's address is : Mumbai";
						cout<<"\nThe Branch Location is : Andheri";
						cout<<"\nAccount number is : 5678";
						cout<<"\n\nPresent available balance  : RS "<<balance;
						cout<<"\n\nPRESS ANY KEY TO RETURN TO THE MAIN MENU";
						break;
					case(0):
						cout<<"\n Thanks for visiting the ATM\n Have a great day!!!";
						exit(0);
						break;
				}
		
		}
	

}
		
			else
			{
				cout<<"\n------------- THANK YOU ----------------------";
				cout<<"\nYou have made your attempt which failed !! No more attempts allowed!! Sorry!!";
			}
		
	  }

};

     
    int main()
    {
    	Firstscreen obj;
    	return 0;
    	
	}
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
	