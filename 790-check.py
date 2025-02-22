
####### bad

class Solution:
    def numTilings(self, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(n+1)]
        if n<=2 : return n
        if n == 3: return 5  

        dp = [0] * (n + 1)
        dp[1], dp[2], dp[3] = 1, 2, 5  # Base cases

        for i in range(4, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3] )% (10**9+7)

        return dp[n]% (10**9+7)
