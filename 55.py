class Solution:
    """
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_jump = [False] * n
        max_jump[-1] = True  
        for i in range(n - 2, -1, -1):  
            furthest_jump = min(i + nums[i], n - 1)  
            for j in range(i + 1, furthest_jump + 1):  
                if max_jump[j]:  
                    max_jump[i] = True
                    break  

        return max_jump[0]
    """
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False
