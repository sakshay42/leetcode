class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n=len(matrix)
        if n==1: return(matrix[0][0])
        out = matrix[0]
        for i in range(1,n):
            z = [0]*n
            for j in range(n):
                z[j] = matrix[i][j] + min(out[max(j-1,0)], out[j], out[min(j+1,n-1)])
            out = z
        return(min(out))


## modify matrix directly to get O(1) space solution
