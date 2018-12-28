def Main():
	exp = input("Enter the expression:")
	#exp = '((A+B)-C*(D/E))+F'
	stack = []
	print("The Postfix Expression is: ",end="")
	infixtopost(stack, exp)

def precedence(op):
	if (op =='+' or op == '-'):
		return 0
	elif (op == '*' or op == '/'):
		return 1
	elif (op == '^'):
		return 3
	else:
		return 2

def infixtopost(stack, exp):
	for char in exp:
		#print(stack)
		if (char.isalpha()):
			print(char,end="")
		else:
			if (char == '+' or char == '-' or char =='*' or char == '/' or char == '^'):
				#print(char)
				if (not stack):
					stack.append(char)
				else:
					if ((precedence(stack[-1]) >= precedence(char)) and stack[-1]!='(' and stack[-1]!=')'):
						while (stack and (precedence(stack[-1]) >= precedence(char)) and stack[-1]!='(' and stack[-1]!=')' ):
							print(stack[-1],end="")
							stack.pop()
						stack.append(char)
					else:
						stack.append(char)
			else:
				if (char == '('):
					stack.append(char)
				else:
					if (char == ')'):
						while (stack[-1]!='('):
							print(stack[-1],end="")
							stack.pop()
						stack.pop()
	while (stack):
		print(stack.pop(),end="")


if __name__ == '__main__':
	Main()
