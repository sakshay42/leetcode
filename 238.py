class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1] * n  # This will store the final out

        # left 
        left_product = 1
        for i in range(n):
            out[i] = left_product
            left_product *= nums[i]

        #right 
        right_product = 1
        for i in range(n-1, -1, -1):
            out[i] *= right_product
            right_product *= nums[i]

        return out






"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]* len(nums)
        right = [1]* len(nums)
        n= len(nums)
        for i in range(1,n):
            left[i] = left[i-1]*nums[i-1]
        for i in range(1,n):
            right[n-i-1] = right[n-i]*nums[n-i]
            
        return [left[i]*right[i] for i in range(n)]
"""
