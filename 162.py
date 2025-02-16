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
