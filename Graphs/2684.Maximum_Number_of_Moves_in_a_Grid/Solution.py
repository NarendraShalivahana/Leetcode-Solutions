2684.Maximum_Number_of_Moves_in_a_Grid
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        dp=[[None for _ in range(m)] for _ in range(n)]
        
        def solve(grid,i,j,n,m,prev,maxi,memo):
            if i<0 or i>=n or j<0 or j>=m:
                return 0
            if grid[i][j]==-1:
                return 0
            if grid[i][j]<=prev:
                return 0
            if memo[i][j]!=None:
                return memo[i][j]
            else:
                cur=grid[i][j]
                grid[i][j]=-1
                s1=1+solve(grid,i-1,j+1,n,m,cur,maxi,memo)
                s2=1+solve(grid,i,j+1,n,m,cur,maxi,memo)
                s3=1+solve(grid,i+1,j+1,n,m,cur,maxi,memo)
                grid[i][j]=cur
            memo[i][j]=max(s1,s2,s3)
            return memo[i][j]
            
        maxi=0
        for i in range(n):
            maxi=max(maxi,solve(grid,i,0,n,m,-1,[0],dp))
        return maxi-1
            
        
