class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [0]*len(nums)
        curr = 0
        total = sum(nums)
        for i in range(len(nums)):
            if curr == total-nums[i]-curr:
                return i
            curr += nums[i]
        return -1
