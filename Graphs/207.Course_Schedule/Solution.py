
class Solution:
    def canFinish(self, C: int, pre: List[List[int]]) -> bool:
        def f(cur,g,vis):
            if vis[cur]==True:
                return False
            vis[cur]=True
            for node in g[cur]:
                if f(node,g,vis)==False:
                    return False
            vis[cur]=False
            g[cur]=[]
            return True

        g=[[] for _ in range(C)]
        for i,j in pre:
            g[j].append(i)
        
        vis=[False for _ in range(C)]
        for i in range(C):
            if f(i,g,vis)==False:
                return False
        return True

        
