def sort_numbers(arr):
    zero_element, one_element, two_element = 0,0,0
    for i in arr:
        if i == 0:
            zero_element+=1
        elif i == 1:
            one_element+=1
        else:
            two_element+=1
    i = 0
    while i < zero_element:
        arr[i] = 0
        i+=1
    print(arr)
    while i < (zero_element + one_element):
        arr[i] = 1
        i+=1
    print(arr)
    while i < len(arr):
        arr[i] = 2
        i+=1
    return arr



arr = [0,0,1,0,2,0,1,2,0,1]

print(sort_numbers(arr))