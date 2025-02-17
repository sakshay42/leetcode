class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2: return(n)
        prev = 1
        current = 2
        for i in range(n-2):
            prev,current = current, prev+current
        return current
