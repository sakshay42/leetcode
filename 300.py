class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        out = [1]+[0]*(n-1)

        for i in range(1,n):
            z = 0
            for j in range(i):
                if nums[j]< nums[i]:
                    z = max(z,out[j])
            out[i] = z+1
        return max(out)
