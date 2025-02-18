class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev =0
        current = 0
        n = len(cost)
        for i in range(2,n+1):
            prev,current = current, min(prev+cost[i-2],current+cost[i-1])
        return(current)
