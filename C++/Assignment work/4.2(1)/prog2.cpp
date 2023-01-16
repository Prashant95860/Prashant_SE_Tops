#include<iostream>
using namespace std;

template <typename T>
void sort(T a[],int n)
{
	int pos_min, i;
	T temp;
	for (int i=0;i<n-1;i++)
	{
		pos_min=i;
		for (int j=i+1;j<n;j++)
		{
			if (a[j]<a[pos_min])
pos_min=j;

		}
if(pos_min !=i)
{
	temp=a[i];
	a[i]=a[pos_min];
	a[pos_min]=temp;
}

	}
	cout<<"\nSorted Elements are : ";
	for(i=0;i<n;i++)
	cout<<"\t"<<a[i];
}





int main()
{
int n,i;
int a[10];
{
	
	cout<<"\n Enter how many numbers you wanted to sort : ";
	cin>>n;
	for(i=0;i<n;i++)
	cin>>a[i];
	sort<int>(a,n);
}
	
	return 0;
}