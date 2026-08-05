class Solution:    
    def numIslands(self, grid: List[List[str]]) -> int:        
        I=len(grid)
        J=len(grid[0])
        def land(i,j):
            grid[i][j]='0'

            if i-1>=0 and j<J and grid[i-1][j]=='1':
                land(i-1,j)
            if i+1<I and j<J and grid[i+1][j]=='1':   
                land(i+1,j)
            if i<I and j-1>=0 and grid[i][j-1]=='1': 
                land(i,j-1)
            if i<I and j+1<J and grid[i][j+1]=='1':
                land(i,j+1)
            return 1 
        count=0           

            
        for i in range(I):
            for j in range(J):
                if grid[i][j]=='1':
                    count+=land(i,j)
        return count            



        
        