"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out =0
        left =0
        for right in range(1,len(prices)):
            if prices[right] < prices[right-1]:
                out += prices[right-1]-prices[left]
                left = right
            if right == len(prices)-1:
                out += prices[right]-prices[left]
        return out
  """













class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out =0
        for right in range(1,len(prices)):
            if prices[right] > prices[right-1]:
                out += prices[right]-prices[right-1]
        return out
