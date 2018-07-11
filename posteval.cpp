#include <iostream>
#include <stack>

using namespace std;

int eval(char exp[],stack<int> st)
{
	int i = 0;
	int ch;
	int n1,n2;

	while(exp[i]!='\0')
	{
		ch = exp[i];

		if (isdigit(ch))
		{
			st.push(ch - 48);
		}
		else
		{
			n1 = st.top();
			st.pop();
			n2 = st.top();
			st.pop();
			switch (ch)
			{
				case '+':st.push(n2+n1);
						break;
				case '-':st.push(n2-n1);
						break;
				case '*':st.push(n2*n1);
						break;
				case '/':st.push(n2/n1);
						break;
			}
		}
		i++;
	}
	return st.top();
}

int main(void)
{
	char exp[30] = "231*+9-";
	stack<int> st;
	int result = eval(exp,st);
	cout<<result;
	return 0;
}
