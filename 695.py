class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        def dfs_area(i,j):
            if i<0 or i>= m or j<0 or j>=n or grid[i][j] ==0:
                return 0
            else: 
                grid[i][j] =0
                return (1+ dfs_area(i-1,j)+dfs_area(i+1,j)+dfs_area(i,j-1) + dfs_area(i,j+1))
                
                
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] ==1:
                    max_area = max(max_area,dfs_area(i,j))
        return max_area
        
