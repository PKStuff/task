def cutTheSticks(arr):
    res = []
    while arr:
        print(arr)
        res.append(len(arr))
        min_element = min(arr)
        i = 0
        n = len(arr)
        while i < n:
            arr[i] -= min_element
            if arr[i] == 0:
                arr.pop(i)
                n-=1
                i-=1
            i+=1
    return res




if __name__ == '__main__':
    arr = [5, 4, 4, 2, 2, 8]
    ans = cutTheSticks(arr)
    print(ans)
