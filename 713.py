class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        curr_prod = 1
        total = 0
        left = 0
        for right in range(len(nums)):
            curr_prod *= nums[right]
            while curr_prod >= k and left < right:
                curr_prod = curr_prod//nums[left]
                left +=1
            total += right-left+1 if curr_prod < k else 0
        return total
