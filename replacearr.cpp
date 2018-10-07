/*Replace every array element by multiplication of previous and next*/
#include <iostream>
#include <vector>

using namespace std;

int* rotate(int[],int);

int* rotate(int vec[],int n)
{
	int *arr;
	for(int i = 0; i < n; i++)
	{
		if(i==0 )
		{
			arr[i]=vec[i]*vec[i+1];
		}
		else if(i==(n-1))
		{
			arr[i]=vec[i]*vec[i-1];
		}
		else
		{
			arr[i]=vec[i-1]*vec[i+1];
		}
	}
	return arr;
}

int main(void)
{
	int v[] ={4,5,6,1,2,3};
	for (int i = 0; i < 6; ++i)
	{
		cout<<v[i]<<"\t";
	}
	int *ptr = rotate(v , 6 );
	cout<<"\n"<<"After multiplication:"<<endl;
	for (int i = 0; i < 6; ++i)
	{
		cout<<ptr[i]<<"\t";
	}
	return 0;
}
