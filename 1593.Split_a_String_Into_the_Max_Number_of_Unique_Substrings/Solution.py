class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        dp=[None for _ in range(len(s))]
        def f(ind,s,n,v,dp):
            if ind>=n:
                return 0
            cur=""; maxi=0
            for i in range(ind,n):
                cur+=s[i]
                if cur not in v:
                    v.add(cur)
                    maxi=max(maxi,1+f(i+1,s,n,v,dp))
                    v.remove(cur)
                elif i==n-1:
                    return 0
            return maxi
          
        v=set()
        ans=f(0,s,len(s),v,dp)
        return ans
