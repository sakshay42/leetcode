class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n <= 0:
            return 0
        left, right = 1, n
        while left <= right:
            middle = (left + right) // 2
            total = (middle * (middle + 1)) // 2
            if total == n:
                return middle
            elif total > n:
                right = middle - 1
            else:
                left = middle + 1
        return right  

"""
can do it O(1) if just solve for X(X+1)/2 = n and return floor of X.
"""
