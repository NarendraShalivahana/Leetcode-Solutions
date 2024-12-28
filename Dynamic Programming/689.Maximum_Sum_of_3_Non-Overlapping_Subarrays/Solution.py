689.Maximum_Sum_of_3_Non-Overlapping_Subarrays
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        dp=[[[[],0] for _ in range(3)] for _ in range(n+1)]
        pre=[];r=0
        for i in range(n-1,-1,-1):
            r+=nums[i]
            if i+k<n:
                r-=nums[i+k]
            pre.append(r)
        def com(a1,a2,v1,v2):
            n,m=len(a1),len(a2)
            # i,j=0,0
            # while i<n and j<m and a1[i]==a2[j]:
            #     i+=1
            #     j+=1
            i,j=n-1,m-1
            while i>-1 and j>-1 and a1[i]>a2[j]:
                i-=1
                j-=1
            if i>-1 and j>-1 and a1[i]<a2[j]:
                return [a1,v1]
            return [a2,v2]


        pre=pre[::-1]
        for i in range(n-k,-1,-1):
            for j in range(3):
                a,b=[i],pre[i]
                c,d=dp[i+k][j][0],dp[i+k][j][1]
                e,f=[],0
                if j-1>-1:
                    a=dp[i+k][j-1][0]+a
                    b+=dp[i+k][j-1][1]
                if b==d:
                    q=com(a,c,b,d)
                    e,f=q[0],q[1]
                elif b>d:
                    e,f=a,b
                else:
                    e,f=c,d
                dp[i][j][0],dp[i][j][1]=e,f
                if i+1<n and dp[i][j][1]<dp[i+1][j][1]:
                    # q=com(dp[i][j][0],dp[i+1][j][0],dp[i][j][1],dp[i+1][j][1])
                    dp[i][j][0],dp[i][j][1]=dp[i+1][j][0],dp[i+1][j][1]
                elif  i+1<n and dp[i][j][1]==dp[i+1][j][1]:
                    q=com(dp[i][j][0],dp[i+1][j][0],dp[i][j][1],dp[i+1][j][1])
                    dp[i][j][0],dp[i][j][1]=q[0],q[1]
        res=[];maxi=0
        for i in range(n):
            a,b=dp[i][2][0],dp[i][2][1]
            if maxi==b:
                if maxi!=0:
                    q=com(res,a,maxi,b)
                    res,maxi=q[0],q[1]
                    
            elif maxi<b:
                res=a;maxi=b

        # print(dp,res)
        return res[::-1]


        
