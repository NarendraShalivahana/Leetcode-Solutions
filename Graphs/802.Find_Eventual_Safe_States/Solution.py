802.Find_Eventual_Safe_States

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        cycle=[0 for _ in range(n)]
        vis=cycle.copy()

        def f(cur,adj,vis,cycle):
            if vis[cur]!=0:
                return True
            
            vis[cur]=1
            for i in adj[cur]:
                if f(i,adj,vis,cycle)==True:
                    cycle[cur]=1
                    return True
            vis[cur]=0
            adj[cur]=[]
            return False

        for i in range(n):
            if vis[i]==0:
                f(i,graph,vis,cycle)
        
        res=[]
        for i in range(n):
            if cycle[i]==0:
                res.append(i)
        return res







            
