def Main():
	print("Enter the expression:")
	exp = input()
	list1 = []
	post(list1,exp)
	print(list1)


def post(list1,exp):

	for ch in exp:
		if ch.isdigit():
			list1.append(ch)
		else:
			num1 = int(list1.pop())
			num2 = int(list1.pop())
			if ch == '+':
				list1.append(num1+num2)
			elif ch == '-':
				list1.append(num1-num2)
			elif ch == '*':
				list1.append(num1*num2)
			elif ch == '/':
				list1.append(num1/num2)
			else:
				pass

if __name__ == '__main__':
	Main()
