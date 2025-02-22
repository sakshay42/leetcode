class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
      ###### idea: do the usual kadane to get max sum of subarray.Now do the minimum. Answer = max(sum-min,max)
        def maxSubarraySum(nums):
            res = nums[0]
            total = 0

            for n in nums:
                if total < 0:
                    total = 0

                total += n
                res = max(res, total)
            
            return res

        return max(sum(nums)+maxSubarraySum([-x for x in nums]), maxSubarraySum(nums)) if maxSubarraySum(nums) >0 else maxSubarraySum(nums)
