class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left =1
        right = max(piles)
        total = sum(piles)
        while right >= left:
            middle= (right + left )//2
            time = sum([(middle+x-1)//middle for x in piles])
            if time > h: left = middle + 1
            else: right = middle -1
        return left
    
        
