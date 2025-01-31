1690.Stone_Game_VII
class Solution:
    def stoneGameVII(self, arr: List[int]) -> int:
        n=len(arr)

        #@lru_cache(2000)
        def f(i,j,sum,dp):
            if sum<=0:
                return 0

            if i>=j:
                return 0
            if dp[i][j]!=None:
                return dp[i][j]


            
            a=max(sum-arr[i]-f(i+1,j,sum-arr[i],dp),sum-arr[j]-f(i,j-1,sum-arr[j],dp))
            dp[i][j]=a
                
            return a
        dp=[[None for _ in range(n+1)]for _ in range(n+1)]
        ans=f(0,n-1,sum(arr),dp)
        return ans
