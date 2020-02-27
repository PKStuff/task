def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    L = mergeSort(arr[:mid])
    R = mergeSort(arr[mid:])

    i = j = k = 0
    
    result = []
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            result.append(L[i])
            i+=1
            k+=1
        else:
            result.append(R[j])
            j+=1
            k+=1
    
    while i<len(L):
        result.append(L[i])
        i+=1
        k+=1
    
    while j<len(R):
        result.append(R[j])
        j+=1
        k+=1
    return result


if __name__ == '__main__':
    arr = [3,2,5,7,2,5,7]

    print(mergeSort(arr))

