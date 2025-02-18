class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rows = len(matrix)
        columns = len(matrix[0])
        
        for i in range(1,rows):
            for j in range(1,columns):
                if matrix[i][j] != matrix [i-1][j-1]: return False
        return True        
