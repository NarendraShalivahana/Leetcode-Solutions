GFG-Subset_Sum_Problem
class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        dp=[[None for _ in range(sum+1)]for _ in range(N+1)]
        def f(sum, ind, arr, N, dp):
            if sum==0:
                return True
            if ind>=N or sum<0:
                return False
            if dp[ind][sum]!=None:
                return dp[ind][sum]
            a=f(sum-arr[ind],ind+1,arr,N,dp)
            b=f(sum,ind+1,arr,N,dp)
            dp[ind][sum]=a or b
            return a or b
        res=f(sum, 0, arr, N,dp)
        return res
