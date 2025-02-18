class Solution:
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev =0
        current = 0
        n = len(cost)
        for i in range(2,n+1):
            prev,current = current, min(prev+cost[i-2],current+cost[i-1])
        return(current)
        """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        stair_cost = [0]*(n+1)
        for i in range(2,n+1):
            stair_cost[i] = min(stair_cost[i-1]+cost[i-1],stair_cost[i-2]+cost[i-2])
        return stair_cost[n]
