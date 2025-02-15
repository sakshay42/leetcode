class Solution:
    def check(self, nums: List[int]) -> bool:
        sign_changes = 0
        n = len(nums)
        i=1
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]: #think of placing numbers in a circle
                sign_changes += 1
            if sign_changes > 1:
                return False
        return(True)
