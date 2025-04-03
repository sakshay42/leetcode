class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #go from right to left. Find the first element that is smaller than it's adjacent number
        #also find the number that is greater than above number  and smallest among that.
        #swap places of these two
        #reverse list from the position found in the first step

        i = len(nums)-1
        while i>0 and nums[i-1] >= nums[i]:
            i-=1
        # i-1 is now the index of the first dip
        if i==0: 
            nums.reverse() #if i==0 then the numbers should be 54321 or something similar
            return 
        
        #i is not 0 i.e list is not reverse
        j = len(nums)-1
        while j>= i and nums[j] <= nums[i-1]: 
           j-=1
        
        nums[i-1],nums[j] = nums[j],nums[i-1]
        nums[i:] = reversed(nums[i:])

