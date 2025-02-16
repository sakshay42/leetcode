"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        out = 0
        n = len(nums)
        if n == 1: return(0)
        for i in range(n):
            if i==0: 
                if nums[0] > nums[1]: out = 0
            elif i==n-1:
                if nums[n-2] < nums[n-1]: out = max(out,n-1)
            else: 
                if nums[i-1]< nums[i] and nums[i] > nums[i+1]: 
                    return(max(out,i))
        return(out)
"""

## Binary search - works because no two adjacenet element sare same

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left,right = 0,  n-1
        while left < right:
            middle = (left + right)//2
            if nums[middle] > nums[middle+1]:
                right = middle
            else: 
                left = middle + 1
        return(left)
