def binary(arr, element):
    arr.sort()
    first = 0
    last = len(arr) - 1
    mid = (first + last)//2
#     print(arr)
    while(first <= last):
#         print(mid)
        if arr[mid] == element:
            return mid
            break
        elif element < arr[mid]:
            last = mid - 1
        elif element > arr[mid]:
            first = mid + 1
        mid = (first + last)//2
    return -1

if __name__ == '__main__':
    arr = [2,1,6,3,7,9,4,5,8]
    k = int(input("Enter the number to find:"))
    index = binary(arr, k)
    if index != -1:
        print("Element found at location:{}".format(index))
    else:
        print("Element not found.")
