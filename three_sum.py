def threeSum(nums):
    if len(nums) < 3:
        return []
    nums.sort()
    res = []
    check_set = set()
    for i in range(0, len(nums)-2):
        j, k = i+1, len(nums)-1
        while j < k:
            if (nums[i] + nums[j] + nums[k]) > 0:
                k-=1
            elif (nums[i] + nums[j] + nums[k]) < 0:
                j+=1
            else:
                if (nums[i],nums[j]) not in check_set:
                    res.append([nums[i], nums[j], nums[k]])
                    check_set.add((nums[i],nums[j]))
                j+=1
                k-=1
    return res

nums = [-2,0,0,2,2]
print(threeSum(nums))
