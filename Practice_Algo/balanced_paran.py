from stack_list import Stack

def check_balanced_parathensis(input):
    st1 = Stack()
    for i in input:
        if i == '(':
            st1.push(i)
        elif i == ')':
            if st1.top_data() != -1:
                st1.pop()
            else:
                return -2
                break
    return st1.top_data()
        

if __name__ == '__main__':
    input = '(())())'
    result = check_balanced_parathensis(input)
    if result == -1:
        print("Balanced Paranthesis....")
    else:
        print("Not balanced.....")