def removeDuplicates(nums):
    n = len(nums)
    i = 0
    while i < n:
        j = i+1 if i < (n-1) else i
        if i != j and nums[i] == nums[j]:
            del nums[j]
            n-=1
        else:
            i+=1
    return len(nums)



nums = [1,1,2]

print(removeDuplicates(nums))
