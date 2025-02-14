class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n= len(nums)
        top = 0
        bottom = 0
        
        #wait till you find a non-val number (bottom) and change it with val number(top).
        while bottom < n:
            if nums[bottom]!=val: 
                nums[top] = nums[bottom]
                top +=1
            bottom +=1
        return(top)
               
