class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_dict = {}
        sum_arr = 0
        count = 0
        if len(nums) == 0:
            return 0
        for i in range(0,len(nums)):
            sum_arr+=nums[i]
            if sum_arr == k:
                count+=1
            if (sum_arr - k) in sum_dict.keys():
                count+=sum_dict[sum_arr - k]
            if sum_arr in sum_dict.keys():
                sum_dict[sum_arr]+=1
            else:
                sum_dict[sum_arr]=1
        return count
