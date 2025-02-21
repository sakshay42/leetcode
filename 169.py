class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]
       
    """
        #Bayer Moore voting
        count, candidate = 0, None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate
    """

    """ #hashmaps

        n = len(nums)
        z = {}
        for i in nums:
            z[i] = z.get(i,0) +1
            if z[i] > n//2:
                return i
    """   
