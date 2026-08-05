class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        c=[]
        I=len(grid)
        J=len(grid[0])
        def land(i,j):
            count=0
            grid[i][j]=0
            count+=1
        

            if i-1>=0 and j<J and grid[i-1][j]==1:
                count+=land(i-1,j)
            if i+1<I and j<J and grid[i+1][j]==1:   
                count+=land(i+1,j)
            if i<I and j-1>=0 and grid[i][j-1]==1: 
                count+=land(i,j-1)
            if i<I and j+1<J and grid[i][j+1]==1:
                count+=land(i,j+1)
            return count 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    c.append(land(i,j))
        if not c:
            return 0            
        return max(c)            


        