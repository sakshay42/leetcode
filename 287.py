class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        uniques = set()
        for i in nums:
            if i in uniques:
                return i
            uniques.add(i)
