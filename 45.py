class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        spots = [float("inf")]*(n-1) + [0]
        for i in range(n-2,-1,-1):
            if nums[i] > 0: 
                for j in range(i+1, min(i+nums[i]+1, n)): 
                    spots[i] = min(spots[i], spots[j] + 1)
        return spots[0]
