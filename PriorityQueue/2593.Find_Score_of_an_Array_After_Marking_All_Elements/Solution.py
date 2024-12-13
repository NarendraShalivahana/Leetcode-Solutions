2593.Find_Score_of_an_Array_After_Marking_All_Elements
class Solution:
    def findScore(self, nums: List[int]) -> int:
        from heapq import heappush,heappop
        pq=[]
        n=len(nums)
        for i in range(n):
            if i==0:
                heappush(pq,(nums[i],i,[i,i+1]))
            elif i==n-1:
                heappush(pq,(nums[i],i,[i,i-1]))
            else:
                heappush(pq,(nums[i],i,[i,i+1,i-1]))
        score=0
        cnt=0
        vis=[False for _ in range(n+1)]
        while cnt<n:
            cur=heappop(pq)
            if vis[cur[1]]==True:
                continue
            score+=cur[0]
            for i in cur[2]:
                if vis[i]==False:
                    vis[i]=True
                    cnt+=1

        return score
        
