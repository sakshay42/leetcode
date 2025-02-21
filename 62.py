class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        out = [[1]*n] + [[0]*n for z in range(m-1)]
        for i in range(1,m):
            for j in range(n):
                if j==0:
                    out[i][j] = out[i-1][j]
                else:
                    out[i][j] = out[i-1][j] + out[i][j-1]
        return out[m-1][n-1]
