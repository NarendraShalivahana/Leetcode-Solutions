983.Minimum_Cost_For_Tickets
class Solution:
    def mincostTickets(self, days: List[int], c: List[int]) -> int:

        n=len(days)
        dp=[None for _ in range(n+1)]
        def f(pos,n,dp):
            if pos>n-1 :
                return 0
            #print(pos)
            if dp[pos]!=None:
                return dp[pos]
            
            d=c[0]+f(pos+1,n,dp)
            j=pos
            for i in range(pos,n):
                if days[i]<days[pos]+7:
                    j=i
            w=c[1]+f(j+1,n,dp)
            k=pos
            for i in range(pos,n):
                if days[i]<days[pos]+30:
                    k=i

            m=c[2]+f(k+1,n,dp)
            #print(d,w,m)
            dp[pos]=min(d,w,m)
            return dp[pos]
        
        ans=f(0,n,dp)
        return ans
