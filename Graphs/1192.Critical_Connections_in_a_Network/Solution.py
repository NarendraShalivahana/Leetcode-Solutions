1192.Critical_Connections_in_a_Network

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def f(cur, rank, prev, adj, low,res):
            low[cur]=rank
            for node in adj[cur]:
                if node==prev:
                    continue
                if low[node]==0:
                    f(node, rank+1, cur, adj, low, res)
                low[cur]=min(low[cur],low[node])
                if low[node]>=rank+1:
                    res.append([cur,node])
            return res
        adj=collections.defaultdict(list)
        for i,j in connections:
            adj[i].append(j)
            adj[j].append(i)
        res=[]
        low=[0 for _ in range(n)]
        f(0, 1, -1, adj, low, res)
        return res
