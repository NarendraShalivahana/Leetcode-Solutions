312.Burst_Balloons
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n=len(nums)
        nums=[1]+nums+[1]
        #n=len(nums)
        dp=[[0 for _ in range(n+2)] for _ in range(n+2)]
        
        for i in range(n,0,-1):
            for j in range(i,n+1):
                
                maxi=float('-inf')
                for k in range(i,j+1):
                    cur=nums[i-1]*nums[k]*nums[j+1]+dp[i][k-1]+dp[k+1][j]
                    maxi=max(maxi,cur)
                dp[i][j]=maxi
        #print(dp)
        return dp[1][n]
        
    
                
                
