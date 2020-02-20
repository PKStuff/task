def equalizeArray(arr):
    dict = {}
    for i in arr:
        if i in dict:
            dict[i]+=1
        else:
            dict[i] = 1
    all_values = list(dict.values())
    print(sum((sorted(all_values))[:len(all_values)-1]))
    

arr = [3, 3, 2, 1, 3]
equalizeArray(arr)
