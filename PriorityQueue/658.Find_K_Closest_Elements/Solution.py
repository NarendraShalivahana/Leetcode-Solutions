658.Find_K_Closest_Elements
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        from heapq import heappush,heappop,heapify
        pq=[]
        for i in range(len(arr)):
            cur=abs(arr[i]-x)
            heappush(pq,(cur,arr[i]))
        res=[]
        while k>0:
            res.append(heappop(pq)[1])
            k-=1
        res.sort()
        return res

        
