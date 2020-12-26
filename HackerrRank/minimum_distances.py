def minimumDistances(a):
    d1 = {}
    for i in range(0, len(a)):
        if a[i] in d1.keys():
            d1[a[i]].append(i)
        else:
            l1 = []
            l1.append(i)
            d1[a[i]] = l1
    min1 = 0
    flag = True
    for key, value in d1.items():
        if len(value) > 1:
            if len(value) == 2:
                if flag:
                    min1 = (value[1]-value[0])
                    flag = False
                if (value[1]-value[0]) < min1:
                    min1 = (value[1]-value[0])
            else:
                for j in range(0, len(value)-1):
                    if (value[j+1] - value[j]) < min1:
                        min1 = (value[j+1] - value[j])
    if min1 == 0:
        return -1
    return min1
