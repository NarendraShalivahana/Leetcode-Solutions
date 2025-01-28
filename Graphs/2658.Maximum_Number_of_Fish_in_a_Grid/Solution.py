2658.Maximum_Number_of_Fish_in_a_Grid
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        n,m=len(grid),len(grid[0])
        vis=[[False for _ in range(m)] for _ in range(n)]
        
        def f(i,j,vis,n,m):
            if i<0 or i>=n or j<0 or j>=m:
                return 0
            if grid[i][j]==0:
                return 0
            if vis[i][j]==True:
                return 0
            # print(1)
            vis[i][j]=True
            a=f(i+1,j,vis,n,m)
            b=f(i-1,j,vis,n,m)
            c=f(i,j+1,vis,n,m)
            d=f(i,j-1,vis,n,m)
            cur=grid[i][j]+a+b+c+d
            return cur
        
        maxi=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0 and vis[i][j]==False:
                    cur=f(i,j,vis,n,m)
                    maxi=max(maxi,cur)
                    # print(maxi)
        return maxi
        
