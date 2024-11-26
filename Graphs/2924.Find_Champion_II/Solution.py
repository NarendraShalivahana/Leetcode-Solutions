2924.Find_Champion_II
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        deg=[0 for _ in range(n)]
        for u,v in edges:
            deg[v]+=1
        cnt=0;ans=-1
        for i in range(n):
            if deg[i]==0:
                cnt+=1
                ans=i
        if cnt==1:
            return ans
        return -1
        
