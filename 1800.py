class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
       n = len(nums)
       left =0
       out = nums[0]
       current = nums[0]
       for right in range(1,n):
            if nums[right-1] < nums[right]: 
                current +=nums[right]
                out = max(out,current)
            else: 
                left = right
                out = max(out,current)
                current = nums[right]

       return(out)
