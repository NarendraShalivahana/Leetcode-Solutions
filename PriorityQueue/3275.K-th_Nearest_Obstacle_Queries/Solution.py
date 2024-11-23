3275.K-th_Nearest_Obstacle_Queries
class Solution:
    def resultsArray(self, qs: List[List[int]], k: int) -> List[int]:
        from heapq import heappush, heappop
        res=[];pq=[]
        for i in range(len(qs)):
            heappush(pq,-1*(abs(qs[i][0])+abs(qs[i][1])))
            if len(pq)>k:
                heappop(pq)
            if len(pq)==k:
                res.append(-1*pq[0])
            else:
                res.append(-1)
        return res
