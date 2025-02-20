class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        counter =set()
        for i in nums:
            if i in counter: return True
            else: counter.add(i)
        return False"""

        return len(nums) != len(set(nums))

