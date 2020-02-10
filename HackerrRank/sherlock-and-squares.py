import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    count = 0
    num = 0
    flag = False
    for num in range(a,b+1):
        if math.sqrt(num)%1==0.0:
            flag = True
            break
    if flag:
        num1 = int(math.sqrt(num))
        num1+=1
        while int(num) < b+1:
            num = num1*num1
            num1+=1
            count+=1
    return count
a = 69
b = 360
print(square(a,b)
