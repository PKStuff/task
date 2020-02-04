def func(keyboards, drives, b):
    keyboards.sort(reverse=True)
    drives.sort(reverse=True)
    if keyboards[-1] + drives[-1] > b:
        return -1
    else:
        if keyboards[-1] >= drives[-1]:
            first = keyboards
            second = drives
        else:
            first = drives
            second = keyboards
        i = 0; j = len(second)-1
        big = 0
        flag = 0
        while(i<len(first)):
            while j> 0:
                if first[i] + second[j] > b:
                    break
                if first[i] + second[j] <= b:
                    if first[i] + second[j] > big:
                        big = first[i] + second[j]
                j-=1
            i+=1
        return big
if __name__ == '__main__':
    b = 60; n = 3; m = 3
    k = [40,50,60]
    u = [5,8,12]
    print(func(k,u,b))
