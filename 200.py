class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n=len(grid[0])

        def bfs(i,j):
            if i<0 or i>m-1 or j<0 or j> n-1 or grid[i][j] =="0":
                return 
            else: 
                grid[i][j] = "0"
                bfs(i-1,j)
                bfs(i+1,j)
                bfs(i,j-1)
                bfs(i,j+1)
        
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    islands +=1
                    bfs(i,j)
        return islands
