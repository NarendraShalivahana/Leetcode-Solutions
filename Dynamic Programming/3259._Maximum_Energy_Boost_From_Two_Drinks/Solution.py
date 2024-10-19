class Solution:
    def maxEnergyBoost(self, A: List[int], B: List[int]) -> int:
        n=len(A)
        dp1=[0 for _ in range(n)]
        dp2=[0 for _ in range(n)]
        for i in range(n):
            cur1=A[i]+dp1[i-1];cur2=B[i]+dp2[i-1]
            if i-2>=0:
                cur1=max(cur1,A[i]+dp2[i-2])
                cur2=max(cur2,B[i]+dp1[i-2])
            dp1[i]=cur1;dp2[i]=cur2
        return max(dp1[n-1],dp2[n-1])
            
        
