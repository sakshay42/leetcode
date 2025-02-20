class Solution(object):
    def knightProbability(self, n, k, row, column):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        if k == 0:
            return 1.0  
        
        moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), 
                 (1, -2), (1, 2), (2, -1), (2, 1)]

        
        prev = [[1.0] * n for _ in range(n)]
        
        
        for m in range(k):
            current = [[0.0] * n for _ in range(n)]

            for i in range(n):
                for j in range(n):
                    prob = 0.0  
                    for dx, dy in moves:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n:  
                            prob += prev[ni][nj] / 8.0  # Each move has 1/8 chance
                    current[i][j] = prob

         
            prev = current 
 

        return prev[row][column]  
