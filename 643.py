class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k]) #intial window of size k
        out_max = window_sum
        for i in range(k,len(nums)):
            window_sum = window_sum + nums[i] - nums[i-k]
            if window_sum > out_max: out_max = window_sum #if you find a new max then change it
        return(out_max/k)

