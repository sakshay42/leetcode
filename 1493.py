class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        out = left = 0
        zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1 
            out = max(out, right - left + 1)

        return out - 1 
