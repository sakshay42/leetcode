class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n-1
        out = []
        while left <= right:
              x = nums[left]**2
              y = nums[right]**2
              if x >= y: 
                out = [x] + out
                left += 1
              else: 
                out = [y]+out
                right -=1
        return(out)
