684.Redundant_Connection
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n=len(edges)
        adj=[[] for _ in range(n+1)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        

        def f(cur,par,vis,adj,v):
            if vis[cur]==True:
                return True
            
            vis[cur]=True
            for node in adj[cur]:
                if node!=par:
                    if f(node,cur,vis,adj,v)==True:
                        v.add((cur,node))
                        v.add((node,cur))
            vis[cur]=False
            return False
        

        v=set()
        vis=[False for _ in range(n+1)]
        for i in range(1,n):
            f(i,-1,vis,adj,v)
        # print(v)
        for i in range(n-1,-1,-1):
            if tuple(edges[i]) in v:
                return edges[i]










