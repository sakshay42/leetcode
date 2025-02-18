class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        left =0
        right= (num_rows*num_cols)-1
        while left <= right:
            middle = (left+right)//2
            middle_row = middle//num_cols
            middle_col = middle%num_cols
            
            if matrix[middle_row][middle_col] == target:
                return(True)
            elif matrix[middle_row][middle_col] > target:
                 right = middle-1
            else: left = middle + 1
        return(False)
