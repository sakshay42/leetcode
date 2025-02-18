class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out = 0
        current_min = prices[0]
        for i in prices[1:]:
            if i-current_min > 0: out = max(out,i-current_min)
            else: current_min = i
        return out
