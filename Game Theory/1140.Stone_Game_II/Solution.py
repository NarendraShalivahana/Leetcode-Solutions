1140.Stone_Game_II
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n=len(piles)
        @lru_cache(None)
        def f(p,n,m):
            if p>=n:
                return 0
            cur,x=0,0
            maxi=float('-inf')
            for i in range(p,min(n,p+m*2)):
                cur+=piles[i]
                x+=1
                m=max(x,m)
                maxi=max(maxi,cur-f(i+1,n,m))
            return maxi
        

        ans=f(0,n,1)

        return (ans+sum(piles))//2
                
