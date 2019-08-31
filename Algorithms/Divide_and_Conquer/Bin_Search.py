import math
def rec_binary(arr,l,h,key):

    if l==h or l<0 or h<0:
        if arr[l]==key:
            return l
        else:
            return -1
    else:
        mid = math.floor((l+h)/2)
        if (arr[mid]==key):
            return mid
        if key < arr[mid]:
            return rec_binary(arr,l,mid-1,key)
        else:
            return rec_binary(arr,mid+1,h,key)

if __name__ == '__main__':
    arr = [23,15,56,25,75,67,27,686,57,76,24,68,132]
    key = int(input("Enter the key:"))
    arr.sort()
    l,h= 0,len(arr)-1
    result = rec_binary(arr,l,h,key)
    if result >= 0:
        print("Element found at location:{}".format(result))
    else:
        print("Element not found.")
