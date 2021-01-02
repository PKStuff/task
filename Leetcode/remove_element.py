def removeElement(nums, val):
    i, j = 0, 0
    n = len(nums)
    if n > 0:
        while i < (n-1):
            if nums[i] == val:
                i+=1
                del nums[j]
                n-=1
                if len(nums) > 0:
                    i=-1
                    j=i
            else:
                i+=1
                j+=1
        if len(nums) > 0 and nums[i] == val:
            i-=1
            del nums[j]
    return len(nums)
nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums, val))
