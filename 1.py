class Solution:
    '''     Brute Force
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         l = len(nums)
         for i in range(0,l):
            for j in range(i+1,l):
                if nums[i]+nums[j] == target:  
                    
                 return([i,j]) 
        '''
    
    ## Hashmap or pair-index 

    def twoSum(self, nums: List[int], target: int) -> List[int]:
         pair_index = {} #contains the number and it's index
         for ind,num in enumerate(nums): #has info of both num and index
            if target - num in pair_index: 
                return([pair_index[target - num],ind])
            else: pair_index[num] = ind #add the index as it is
