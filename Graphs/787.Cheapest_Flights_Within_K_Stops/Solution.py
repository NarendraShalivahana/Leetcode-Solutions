787.Cheapest_Flights_Within_K_Stops
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        from collections import deque
        adj=[[] for _ in range(n)]
        for u,v,c in flights:
            adj[u].append([v,c])
        cost=[float('inf') for _ in range(n)]
        dq=deque([])
        dq.append([src,0])
        while dq and k>-2:
            arr=[]
            while dq:
                node,c=dq.popleft()
                if cost[node]>c:
                    cost[node]=c
                    for cur in adj[node]:
                        arr.append([cur[0],cur[1]+c])
            dq+=arr
            k-=1
        if cost[dst]==float('inf'):
            return -1
        return cost[dst]
        
