def searchRange(nums, target):
    i, j = 0, len(nums)-1
    mid = (i+j)//2
    fount_pos = None
    while i <= j:
        if nums[mid] == target:
            fount_pos = mid
            break
        elif nums[mid] < target:
            i = mid + 1
        else:
            j = mid - 1
        mid = (i+j)//2
    if fount_pos is None:
        return [-1, -1]
    i, j = fount_pos, fount_pos
    l1 = []
    while i >= 0 and nums[i] == target:
        i-=1
    l1.append(i+1)
    while j <= len(nums)-1 and nums[j] == target:
        j+=1
    l1.append(j-1)
    return l1


nums, target = [5,7,7,8,8,10],  8

print(searchRange(nums, target))
