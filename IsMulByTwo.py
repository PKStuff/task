def isTwo(number):

    if number == 1:
        return True
    else:
        flag = True
        while(number != 1):
            number/=2
            remainder = number % 2
            if number == 1:
                flag = True
            elif remainder > 0:
                flag = False
                break
    return flag

if __name__ == '__main__':
    for num in range(1,100001):
        if isTwo(num):
            print(num, end=" ")
       
'''
OUTPUT:
PS C:\Projects\Python> python .\sample.py
1 2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536
'''
