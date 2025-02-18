class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        max_house = [nums[0]] + ([0]* (n-1))
        for i in range(1,n):
            if i==1: max_house[1] = max(nums[0],nums[1])
            else: max_house[i] = max(max_house[i-2]+nums[i], max_house[i-1])
        return(max_house[n-1])
