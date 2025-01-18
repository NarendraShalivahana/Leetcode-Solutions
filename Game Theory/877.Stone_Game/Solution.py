877.Stone_Game
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        n=len(piles)
        def f(ali,bob,i,j,arr,flag,dp):
            if i>=j:
                if ali>bob:
                    return True
                return False
            if dp[i][j][flag]!=None:
                return dp[i][j][flag]

            ans1,ans2=False,False
            if flag==0:
                ans1=f(ali+arr[i],bob,i+1,j,arr,1,dp) or f(ali+arr[j],bob,i,j-1,arr,0,dp)
            
            elif flag==1:
                ans2=f(ali,bob+arr[i],i+1,j,arr,0,dp) or f(ali,bob+arr[j],i,j-1,arr,0,dp)
            ans=ans1 or ans2
            dp[i][j][flag]=ans
            return ans
        dp=[[[None for _ in range(2)] for _ in range(n+1)] for _ in range(n+1)]
        ans=f(0,0,0,n-1,piles,0,dp)
        return ans
            
            



        
