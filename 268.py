class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        return(  (((n)*(n+1))//2)-total)


#sum of 0,1,...n = n(n+1)/2 and subtract the total sum. Any way you have to have an idea of every number in the list so best solution is O(n)


