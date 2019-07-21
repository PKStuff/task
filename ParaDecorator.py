import time
def Calculate(name):
    print(name)
    print("Inside Decorator")
    def inside(func):
        def wrapper(*args,**kargs):
            start_time = time.time()
            func(*args,**kargs)
            end_time = time.time()
            print("Function:{} taken:{} amount of time.".format(func.__name__,end_time-start_time))
        return wrapper
    return inside

@Calculate('Pradip')
def addFunc(a,b):
    print(a+b)

if __name__ == '__main__':
    addFunc(100,123)

'''
Pradip
Inside Decorator
223
Function:addFunc taken:0.002074718475341797 amount of time.
'''
