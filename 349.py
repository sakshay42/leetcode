from collections import defaultdict, Counter
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = Counter(nums1)
        nums2 = Counter(nums2)
        intersection = set()
        for i in nums1:
            if i in nums2:
                intersection.add(i)
        return list(intersection)
