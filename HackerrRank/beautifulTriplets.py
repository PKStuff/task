def beautifulTriplets(d, arr):
    i = 0
    count = 0
    while i < len(arr):
        j = i
        flag = False
        if (arr[i] + d) in arr[i:]:
            j = arr.index(arr[j]+d)
            if (arr[j] + d) in arr[j:]:
                flag = True
        if flag:
            count+=1
        i+=1
    return count
