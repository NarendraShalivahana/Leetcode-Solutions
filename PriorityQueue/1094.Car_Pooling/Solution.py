1094.Car_Pooling
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        from heapq import heappush,heappop,heapify
        arr=[];dep=[];maxi=0;n=len(trips)
        for i in range(n):
            arr.append([trips[i][1],trips[i][0]])
            dep.append([trips[i][2],trips[i][0]])
            maxi=max(maxi,trips[i][2])
        cur=0;heapify(arr);heapify(dep)
        for i in range(maxi+1):
            while arr and arr[0][0]<=i:
                cur+=heappop(arr)[1]
            while dep and dep[0][0]<=i:
                cur-=heappop(dep)[1]
            if cur>capacity:
                return False
        return True
            
        
        
        
