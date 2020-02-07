def func(n):
    d1 = {}
    fact = 1
    for i in range(1,n+1):
        if i in d1.keys():
            fact*=d1[i]
        else:
            fact*=i
            d1[i]=fact
    return fact

print(func(45))
