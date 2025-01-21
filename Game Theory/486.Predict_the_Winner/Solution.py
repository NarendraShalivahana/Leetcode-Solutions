486.Predict_the_Winner
class Solution:
    def PredictTheWinner(self, piles: List[int]) -> bool:
        n=len(piles)
        def f(ali,bob,i,j,arr,flag,dp):
            if i>j:
                return 0
            if dp[i][j][flag]!=None:
                return dp[i][j][flag]

            ans,ans2=False,False
            if flag==0:
                ans=max(arr[i]+f(ali,bob,i+1,j,arr,1,dp),arr[j]+f(ali,bob,i,j-1,arr,1,dp))
                #return ans
            elif flag==1:
                ans2=min(-arr[i]+f(ali,bob,i+1,j,arr,0,dp),-arr[j]+f(ali,bob,i,j-1,arr,0,dp))
                #return ans2
            dp[i][j][flag]=ans or ans2
            return dp[i][j][flag]
        dp=[[[None for _ in range(2)]  for _ in range(n+1)] for _ in range(n+1)]
        ans=f(0,0,0,n-1,piles,0,dp)
        return ans>=0
