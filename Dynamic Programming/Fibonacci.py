import time
def outer(func):
    def wrapper(*args, **kargs):
        start_time = time.time()
        result = func(*args, **kargs)
        end_time = time.time()
        print("Time required for the function:{} is:{}".format(func.__name__,(end_time - start_time)))
    return wrapper

@outer
def fib1_not_dynamic(number):
    for num in range(number):
        fib(num)

def fib(n):
    if n <=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

@outer
def fibb_Dynamic(n):
    f = {}
    f[0] = 0
    f[1] = 1
    for i in range(2,n):
        f[i] = f[i-1] + f[i-2]
    return f

if __name__ == '__main__':
    number = int(input("Enter the number:"))
    data = fib1_not_dynamic(number)
    f = fibb_Dynamic(number)
    
'''
PS C:\Projects\Python\Dynamic Programming> python .\Fibonacci.py
Enter the number:23
Time required for the function:fib1_not_dynamic is:0.03125429153442383
Time required for the function:fibb_Dynamic is:0.0
'''