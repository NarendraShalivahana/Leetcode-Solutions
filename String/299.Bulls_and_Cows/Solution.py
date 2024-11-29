299.Bulls_and_Cows
class Solution:
    def getHint(self, s: str, g: str) -> str:
        from collections import Counter
        c=Counter(s)
        x,y=0,0
        n=len(s)
        vis=[False for _ in range(n)]
        for i in range(n):
            
            if s[i]==g[i]:
                x+=1
                c[g[i]]-=1
                vis[i]=True
        # print(c)
        for i in range(n):
            if vis[i]==False and g[i] in c and c[g[i]]>=1:
                # print(g[i],c[g[i]])
                c[g[i]]-=1
                y+=1

        res=str(x)+"A"+str(y)+"B"
        return res
