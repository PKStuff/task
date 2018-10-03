#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric>

using namespace std;

int main(void)
{
	int arr[] = {4,5,2,6,1,7,2,7,4};
 	int size = sizeof(arr) / sizeof(arr[0]) ;
 	
 	vector<int> vec(arr,arr+size);
 	
 	cout<<"vector is:"<<endl;
 	
 	for(int i = 0 ; i<size ;i++)
 	{
 	    cout<<vec[i]<<"\t";
 	}
	sort(vec.begin(),vec.end());
	
	cout<<endl<<"After Sort:"<<endl;
	
	for(int i = 0 ; i<size ;i++)
 	{
 	    cout<<vec[i]<<"\t";
 	}
 	
 	reverse(vec.begin(),vec.end());
 	
 	cout<<endl<<"After reverse:"<<endl;
 	
 	for(int i = 0 ; i<size ;i++)
 	{
 	    cout<<vec[i]<<"\t";
 	}
 	cout<<endl<<"Max Element:"<<*max_element(vec.begin(),vec.end());
 	cout<<endl<<"Min Element:"<<*min_element(vec.begin(),vec.end());
 	
 	cout<<endl<<"The Total is:"<<accumulate(vec.begin(),vec.end(),0);
 	
 	vec.erase(unique(vec.begin(),vec.end()),vec.end());
 	
 	cout<<endl<<"Unique:"<<endl;
 	
 	for(int i = 0 ; i<vec.size() ;i++)
 	{
 	    cout<<vec[i]<<"\t";
 	}
	return 0;
}
