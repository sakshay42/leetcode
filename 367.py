class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        while left <= right: 
            middle = (left + right) //2
            if middle**2 > num: right = middle-1
            elif middle**2 <num: left = middle + 1
            else: return True
        return False
