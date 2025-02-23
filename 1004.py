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
                k-=1 #every time you hit a zero reduce k by 1
            if k<0: #if hits zero that means that you have k zeros (if you have k+i zeros)
                if nums[l] == 0: #delete left number, if left number is 0 then you can add one more zero so k=1
                    k+=1 
                l+=1       #you have to keep moving left pointer
        return r-l+1
