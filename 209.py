class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        out = float('inf') #infinite
        window_sum = 0
        left = 0
        for right in range(0,len(nums)):
            window_sum += nums[right]
            while window_sum >= target:
                out = min(out,right-left+1) 
                window_sum -= nums[left]
                left +=  1
        return(out if out!= float('inf') else 0) #short hand to write if else
