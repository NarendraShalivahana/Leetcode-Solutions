673.Number_of_Longest_Increasing_Subsequence
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1 for _ in range(n)]
        ways=[1 for _ in range(n)]
        maxi=1
        for i in range(n):
            for j in range(i):

                if nums[j]<nums[i] and 1+dp[j]>dp[i]:
                    dp[i]=max(dp[i],1+dp[j])
                    ways[i]=ways[j]
                    
                elif nums[j]<nums[i] and 1+dp[j]==dp[i]:
                    ways[i]+=ways[j]
                maxi=max(maxi,dp[i])
        ans=0
        for i in range(n):
            if dp[i]==maxi:
                ans+=ways[i]
        return ans
        
