""" 83ms
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
"""

""" 68ms
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        out = left = 0
        zero_count =0
        for right in range(len(nums)):
            zero_count += 1-nums[right]
            while zero_count > k:                          #this condition is changed
                zero_count += nums[left]-1
                left = left + 1
            out = max(out,right - left +1)
        return out
"""

""""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        out = left = 0
        zero_count =0
        for right in range(len(nums)):
            zero_count += 1-nums[right]
            while zero_count > k:                          #this condition is changed
                 if nums[left] == 0:
                    zero_count -= 1                       # this changed
                 left += 1  
            out = max(out,right - left +1)
        return out
""""


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=r=0    
        for r in range(len(nums)):
            if nums[r] == 0:
                k-=1
            if k<0:
                if nums[l] == 0:
                    k+=1
                l+=1
        return r-l+1
