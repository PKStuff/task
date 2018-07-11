#include <iostream>
#include <stack>

using namespace std;

int precedence(char op)
{
	if(op == '+' || op == '-')
		return 0;
	else if(op == '*' || op == '/')
		return 1;
	else
		return 2;
}

void infixtopostfix(char exp[],stack<char> st)
{
	int i = 0;
	char ch;
	while(exp[i]!='\0')
	{
		ch = exp[i];

		if (isalpha(ch))
		{
			cout<<ch;
		}
		else
		{
			if (ch == '+' || ch == '-' || ch == '*' || ch =='/')
			{
				if (st.empty())
				{
					st.push(ch);
				}
				else
				{
					if (precedence(ch) <= precedence(st.top()) && st.top() != '(' && st.top() != ')')
					{
						cout<<st.top();	
						st.pop();
						st.push(ch);					
					}
					else
						st.push(ch);
				}
			}
			else
			{
				if(ch == '(')
					st.push(ch);
				else
				{
					if (ch == ')')
					{
						while(st.top()!='(')
						{
							cout<<st.top();
							st.pop();
						}
						st.pop();
					}
				}
			}
		}
		i++;
	}
	while(!st.empty())
	{
		cout<<st.top();
		st.pop();
	}
}

int main()
{
	stack<char> st;
    char exp[] = "A*(B+C)*D";
    infixtopostfix(exp,st);
    return 0;
}
