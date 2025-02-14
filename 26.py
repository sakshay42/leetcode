class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
         out = 0
         top = 0
         bottom = 1
         while bottom < len(nums):
            if nums[top] != nums[bottom]:
                 top +=1
                 nums[top], nums[bottom] = nums[bottom], nums[top]

            bottom +=1
         return(top+1)
