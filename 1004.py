class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        out = left = 0
        zero_count =0
        for right in range(len(nums)):
            zero_count += 1-nums[right]
            while zero_count == k+1:
                zero_count += nums[left]-1
                left = left + 1
            out = max(out,right - left +1)
        return out
